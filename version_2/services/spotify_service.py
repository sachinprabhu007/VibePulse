import os
import random
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv

load_dotenv()

sp = spotipy.Spotify(
    auth_manager=SpotifyClientCredentials(
        client_id=os.getenv("SPOTIFY_CLIENT_ID"),
        client_secret=os.getenv("SPOTIFY_CLIENT_SECRET")
    )
)

def search_tracks(query, limit=10):
    offset = random.randint(0, 50)

    results = sp.search(
        q=query,
        type="track",
        limit=limit,
        offset=offset
    )

    tracks = []
    for t in results["tracks"]["items"]:
        tracks.append({
            "name": t["name"],
            "artist": t["artists"][0]["name"],
            "album": t["album"]["name"],
            "url": t["external_urls"]["spotify"],
            "image": t["album"]["images"][0]["url"]
        })

    return tracks
