import requests
from bs4 import BeautifulSoup
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth


CLIENT_ID = os.environ.get("CLIENT_ID")
CLIENT_SECRET = os.environ.get("CLIENT_SECRET")
REDIRECT_URL = os.environ.get("REDIRECT_URL")
print(CLIENT_ID)
print(CLIENT_SECRET)
print(REDIRECT_URL)

user_date = input("Which year you would like to travel to? Type the date in this format YYYY-MM-DD: ")
HEADER = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36 OPR/123.0.0.0"
}
URL = "https://www.billboard.com/charts/hot-100"
URL_DATE = f"{URL}/{user_date}"

response = requests.get(URL_DATE, headers=HEADER)
response.raise_for_status()
soup = BeautifulSoup(response.text, "html.parser")

songs_tags = soup.select("li ul li h3")
songs = [song.getText().strip() for song in songs_tags]

scope = "playlist-modify-private"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    scope=scope,
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri=REDIRECT_URL,
    show_dialog=True,
    cache_path="token.txt"
))

user_id = sp.current_user()["id"]
year = user_date.split("-")[0]

tracks_uris = []
for song in songs:
    result = sp.search(f"track:{song} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        tracks_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify")

user_playlist = sp.user_playlist_create(user=user_id, name=f"{user_date} Billboard 100", public=False, description="This is for you, my love!")
sp.playlist_add_items(playlist_id=user_playlist["id"], items=tracks_uris, position=0)
