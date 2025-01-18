from bs4 import BeautifulSoup
import requests
import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()

client_id = os.getenv("SPOTIFY_CLIENTID")
client_secret = os.getenv("SPOTIFY_CLIENTSECRET")
redirect_url = os.getenv("SPOTIFY_REDIRECTURL")
spotify_username = os.getenv("SPOTIFY_USERNAME")

date = input("Which year do you want to travel to? Type in the format YYYY-MM-DD: ")
URL = f"https://www.billboard.com/charts/hot-100/{date}/"
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}

response = requests.get(url=URL, headers=header)
billboard_page = response.text


soup = BeautifulSoup(billboard_page, 'html.parser')
song_titles = [song.getText().strip() for song in soup.select("li ul li h3")]
print(song_titles)


#Spotify Authentication
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=client_id,
        client_secret=client_secret,
        show_dialog=True,
        cache_path="token.txt",
        username=spotify_username,
    )
)
user_id = sp.current_user()["id"]

def get_song_urls(song_names):
    song_urls = []

    for song in song_names:
        try:
            #Search on Spotify
            result = sp.search(q=song, type="track", limit=1)

            #Extract url of the first result
            track = result["tracks"]["items"][0]
            song_urls.append(track["external_urls"]["spotify"])
            print(f"Found: {song} -> {track['external_urls']['spotify']}")

        except IndexError:
            print(f"{song} not found :(")

    return song_urls


playlist_name = f"{date} Billboard Hot 100"
playlist_description = "My Scraped Billboard Hot 100"
new_playlist = sp.user_playlist_create(
    user=user_id,
    name=playlist_name,
    public=False,
    description=playlist_description,
)

print(f"Created playlist '{new_playlist['name']}' with ID: {new_playlist['id']}")

song_urls = get_song_urls(song_titles)
print("\nList of Spotify URLs:")
print(song_urls)

track_uris = [url.split("/")[-1] for url in song_urls]
sp.playlist_add_items(playlist_id=new_playlist['id'], items=track_uris)
print(f"Added {len(track_uris)} tracks to the playlist '{new_playlist['name']}'")
