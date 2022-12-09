# this is the AppleMusicToSpotify/app/main.py file...


# Imports 
import app.tajMusic as tm

# Spotify Token Access
import os
from dotenv import load_dotenv

load_dotenv()

spotipy_client_id = os.getenv("client_id")
client_secret = os.getenv("client_secret")
client_credentials_manager = os.getenv("client_credentials_manager")
sp = os.getenv("sp")

# Get XML name
playlist = tm.xml_name()

# Get song list
song_list = []
song_list = tm.song_list_generator(playlist)

# Get artist list
artist_list = []
artist_list =tm.artist_list_generator(playlist)

# Get album list 
album_list = []
album_list = tm.album_list_generator(playlist)

# Get username
my_username = tm.get_username()

# Get playlist name
playlist_name = tm.get_playlist_name()

# Create playlist
my_playlist_id = tm.create_playlist(my_username, playlist_name)

# Get track ID List
track_id_list = []

# Add songs to a playlist
tm.add_to_playlist(song_list, artist_list, album_list, my_username, my_playlist_id, track_id_list)