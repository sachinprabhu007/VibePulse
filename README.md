# 🌟🎧 VibePulse: Tune Into Your Mood 🎵🎹

VibePulse is a lightweight web app that turns a user’s mood or vibe into meaningful music recommendations using the Spotify API.

Describe how you feel — calm, energetic, focused, rainy evening — and VibePulse finds music that fits the moment.

---

## 🚀 Features

- 🎧 Mood-based music discovery  
- ✍️ Natural language vibe input  
- 🎵 Spotify track search  
- 🖼️ Album artwork and artist details  
- 🔗 One-click “Open in Spotify” links  
- 🌐 Deployable on Render or run locally  

---

## 🧠 How It Works

1. User enters a mood or vibe
2. The input is refined into a concise music query
3. Spotify Search API fetches relevant tracks
4. Results are displayed with album art and Spotify links

---

## ⚡ Deployment Guide

### **1. Run Locally**

1. Clone the repository:

```
git clone https://github.com/sachinprabhu007/VibePulse.git
cd VibePulse
```

2. Create a virtual environment and install dependencies:

```
python -m venv env
source env/bin/activate  # macOS/Linux
env\Scripts\activate     # Windows
pip install -r requirements.txt
```

Create your spotify app creds over here - https://developer.spotify.com/

Add your Spotify credentials in a .env file (do not commit this file):

```
SPOTIFY_CLIENT_ID=your_client_id
SPOTIFY_CLIENT_SECRET=your_client_secret
```

Run the app locally:

```
streamlit run app.py
```

Can see the app running on following url 
``` 
http://localhost:8501
```

### 2. Deploy on Render

1. Log in to Render
2. Click New → Web Service and connect your GitHub account.
3. Select the VibePulse repository and choose branch main or can be empty as Render takes it automatically

⚙️Configure the service:

Build Command:

```
pip install -r requirements.txt
```

Start Command:

```
streamlit run app.py --server.port $PORT
```

Add environment variables in Render dashboard (can choose from env file as well):
```
SPOTIFY_CLIENT_ID=your_client_id
SPOTIFY_CLIENT_SECRET=your_client_secret
```

Click Create Web Service — Render will deploy and give a live URL, e.g.:
```
https://vibepulse-acrn.onrender.com/
```
This link is automatically created by Render when the web service is deployed.  
The footer will automatically detect Render as the platform.

---

### 💻 Repository

Source code: https://github.com/sachinprabhu007/VibePulse

### ❤️ Credits

Made with love for music enthusiasts by Sachin Prabhu.
Powered by Streamlit, Spotify, and Hugging Face / Render.

## 📄 License
Please go through [LICENSE](LICENSE) file for details.