import os
import random
import logging
import streamlit as st
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")

# Logging setup
logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Create and cache Spotify client (created once per session)
@st.cache_resource
def get_spotify_client():
    return spotipy.Spotify(
        auth_manager=SpotifyClientCredentials(
            client_id=SPOTIFY_CLIENT_ID,
            client_secret=SPOTIFY_CLIENT_SECRET
        )
    )

def search_tracks(query):
    sp = get_spotify_client()
    response = sp.search(q=query, type="track", limit=10)  # reduced limit for mobile
    items = response.get("tracks", {}).get("items", [])

    random.shuffle(items)
    tracks = []
    for t in items:
        tracks.append({
            "name": t["name"],
            "artist": t["artists"][0]["name"],
            "album": t["album"]["name"],
            "url": t["external_urls"]["spotify"],
            "image": t["album"]["images"][0]["url"]
        })
    return tracks

# Page settings
st.set_page_config(
    page_title="VibePulse",
    layout="centered",
    initial_sidebar_state="collapsed"
)

st.title("🌟🎧 VibePulse: Tune Into Your Mood 🎵🎹")
st.caption("Type a mood, genre, or feeling — we will find the music that fits it.")

# Session state to prevent duplicate logs on reruns
if "last_query" not in st.session_state:
    st.session_state.last_query = None

# Search form (Enter key works)
with st.form("search_form"):
    query = st.text_input(
        "What’s your vibe right now?",
        placeholder="meditative, pop, rainy evening, focus, workout..."
    )
    submitted = st.form_submit_button("🎶 Find my music")

if submitted and query.strip():
    if st.session_state.last_query != query:
        logging.info(f"User searched for: {query}")
        st.session_state.last_query = query

    with st.spinner("🎧 Finding the right vibes for you..."):
        tracks = search_tracks(query)

    logging.info(f"Found {len(tracks)} tracks for query '{query}'")

    if not tracks:
        st.warning("No tracks found. Try a different vibe.")
    else:
        # Mobile-friendly column layout
        screen_width = st.experimental_get_query_params().get("screen_width", [0])[0]
        try:
            screen_width = int(screen_width)
        except:
            screen_width = 0

        cols_count = 1 if screen_width and screen_width < 600 else 2
        cols = st.columns(cols_count)

        for idx, track in enumerate(tracks):
            with cols[idx % cols_count]:
                st.image(track["image"], use_column_width=True)
                st.markdown(f"🎵 **{track['name']}**")
                st.markdown(f"💛 *{track['artist']}*")
                st.caption(f"Album: {track['album']}")
                st.markdown(f"[Open in Spotify]({track['url']})")
                st.markdown("---")

# footer config
def display_footer():
    if os.getenv("HF_SPACE_ID"):
        platform = "Hugging Face Spaces"
        platform_link = "https://huggingface.co/spaces"
    elif os.getenv("RENDER"):
        platform = "Render"
        platform_link = "https://render.com/"
    else:
        platform = None
        platform_link = None

    platform_html = f" &amp; <a href='{platform_link}' target='_blank'>{platform}</a>" if platform else ""

    st.markdown("""
    <div style='text-align: center; color: #666; padding-top: 12px;'>
        <p>🎵 <strong>VibePulse</strong> | Powered by 
            <a href='https://developer.spotify.com/' target='_blank'>Spotify</a>, 
            <a href='https://streamlit.io/' target='_blank'>Streamlit</a>{platform_html}
        </p>
        <p>Made with ❤️ for music enthusiasts</p>
        <p>by <strong>Sachin Prabhu</strong></p>
        <p>🔗 <a href='https://github.com/sachinprabhu007/VibePulse' target='_blank'>View on GitHub</a></p>
    </div>
    """.format(platform_html=platform_html),
    unsafe_allow_html=True
    )

display_footer()
