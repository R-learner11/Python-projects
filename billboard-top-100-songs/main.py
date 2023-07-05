import requests
# import pprint
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
from bs4 import BeautifulSoup

client_id = os.environ.get("spotify_client_id")
client_secret = os.environ.get("spotify_client_secret")
redirect_uri = "http://www.example.com"
scope = "playlist-modify-private"

# creating an input prompt of which date we want the playlist to be created
date = input("Enter the date in YYYY-MM-DD: ")
response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}/")
response_data = response.text

# TODO 1: scrape data from billboard hot 100 for date
# creating a soup of the response_data from billboard hot 100 charts
soup = BeautifulSoup(response_data, "html.parser")
# extract all the name of the songs (100 songs)
songs_list = []
all_songs_ul = soup.find_all(name="ul", class_="lrv-a-unstyle-list lrv-u-flex lrv-u-height-100p lrv-u-flex-direction-column@mobile-max")
for songs in all_songs_ul:
    top_songs = songs.select("#title-of-a-story")[0].text.strip("'\n','\t'")
    songs_list.append(top_songs)

# authorizing
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri= redirect_uri, show_dialog=True, scope=scope, cache_path='token.txt'))

# accessing user_id
user_id = sp.current_user()['id']

# TODO 2: List of song uris
# creating a list of songs uris
song_uris = []
year = date.split('-')[0]
for song in songs_list:
    results = sp.search(q=f"track:{song} year:{year}", type='track', limit=1)
    try:
        uri = results['tracks']['items'][0]['uri']
        print(uri)
        song_uris.append(uri)
    except IndexError:
        print("This song doesnot exist in spotify. Skipped.")

# TODO 3: Creating a playlist
# creating a playlist in spotify using spotipy
playlist_name = f"Billboard hot 100 {date}"
playlist_description = "This is the list of songs of billboard top 100. This brings back all the memories associated" \
                       " with that day, week or era."
playlist = sp.user_playlist_create(user=user_id, name=playlist_name, public=False, description=playlist_description)
playlist_id = playlist['id']

# TODO 1: Add songs to the playlist
# adding songs to the playlist
sp.playlist_add_items(playlist_id=playlist_id, items=song_uris)





