from pprint import pprint

import requests
from bs4 import BeautifulSoup
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

load_dotenv()

URL = "https://www.billboard.com/charts/hot-100/"

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
url = URL + date
response = requests.get(url=url)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")
song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]
print(song_names)

scope = "playlist-modify-private"
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope=scope,
        client_id=os.getenv("SPOTIFY_CLIENT_ID"),
        client_secret=os.getenv("SPOTIFY_CLIENT_SECRET"),
        redirect_uri=os.getenv("SPOTIFY_REDIRECT_URL")
    )
)

user = sp.current_user()
user_id = user["id"]

song_uris = []
year = date[:4]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

# new_playlist = sp.user_playlist_create(
#     user=user_id,
#     name=f"{date} Billboard 100",
#     public="True",
#     collaborative="False"
# )
# playlist_id = new_playlist["id"]

print(",".join(song_uris))

