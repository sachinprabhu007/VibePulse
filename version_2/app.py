import os
import random
import logging

import streamlit as st
from dotenv import load_dotenv
from services.spotify_service import search_tracks
from services.llm_service import refine_query

# Load environment variables
load_dotenv()

# Logging setup
logging.basicConfig(
    filename="logs/app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Page settings
st.set_page_config(
    page_title="🌟 VibePulse",
    layout="wide"
)

st.title("🌟 VibePulse: Your Mood, Your Music")
st.caption("Describe your mood or vibe — we’ll find the music that fits it.")


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

    # Refine query with Gemini Flash 2.5
    with st.spinner("🎵 Refining your vibe..."):
        refined_query = refine_query(query)

    logging.info(f"User mood input: {query}")
    logging.info(f"Refined query from Gemini: {refined_query}")

    # Search Spotify
    with st.spinner("🎧 Finding the right vibes for you..."):
        tracks = search_tracks(refined_query)

    logging.info(f"Found {len(tracks)} tracks for query '{refined_query}'")
    logging.info(f"Tracks data: {tracks}")

    if not tracks:
        st.warning("No tracks found. Try a different vibe.")
    else:
        # Display tracks in two columns like version1
        cols = st.columns(2)
        for idx, track in enumerate(tracks):
            with cols[idx % 2]:
                st.image(track["image"], width=220)
                st.markdown(f"🎵 **{track['name']}**")
                st.markdown(f"💛 *{track['artist']}*")
                st.caption(f"Album: {track['album']}")
                st.markdown(f"[Open in Spotify]({track['url']})")
                st.markdown("---")
