from dotenv import load_dotenv
load_dotenv()

import requests
from pymongo import MongoClient
import os

# Spotify API credentials
CLIENT_ID = os.environ['SPOTIFY_CLIENT_ID']
CLIENT_SECRET = os.environ['SPOTIFY_CLIENT_SECRET']

# MongoDB connection string
MONGODB_URI = os.environ['MONGODB_URI']

# Playlist ID of the top 50 songs
PLAYLIST_ID = os.environ['PLAYLIST_ID']

def get_access_token():
    """
    Get an access token from the Spotify API.

    Returns:
        str: The access token.
    """
    url = 'https://accounts.spotify.com/api/token'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'grant_type': 'client_credentials',
    }
    response = requests.post(url, headers=headers, data=data, auth=(CLIENT_ID, CLIENT_SECRET))
    response_json = response.json()
    access_token = response_json['access_token']
    return access_token

def fetch_songs(access_token):
    """
    Fetch the top 50 songs from the Spotify API.

    Args:
        access_token (str): The access token.

    Returns:
        list: A list of dictionaries containing the song data.
    """
    url = f'https://api.spotify.com/v1/playlists/{PLAYLIST_ID}/tracks'
    headers = {
        'Authorization': f'Bearer {access_token}',
    }
    response = requests.get(url, headers=headers)
    response_json = response.json()
    songs = []
    for i, item in enumerate(response_json['items']):
        track = item['track']
        song = {
            'id': track['id'],
            'name': track['name'],
            'artist': track['artists'][0]['name'],
            'album': track['album']['name'],
            'release_date': track['album']['release_date'],
            'popularity': track['popularity'],
            'duration_ms': track['duration_ms'],
            'position': i + 1,  # add the position of the song in the playlist
        }

        # Get audio features of the track
        audio_features_url = f'https://api.spotify.com/v1/audio-features/{track["id"]}'
        audio_features_response = requests.get(audio_features_url, headers=headers)
        audio_features = audio_features_response.json()
        song.update(audio_features)

        songs.append(song)
    return songs

def store_songs(songs):
    """
    Store the songs in the MongoDB database.

    Args:
        songs (list): A list of dictionaries containing the song data.
    """
    client = MongoClient(MONGODB_URI)
    db = client['chart-tracker']
    collection = db['songs']
    collection.insert_many(songs)


def main():
    """
    The main function of the script.
    """
    access_token = get_access_token()
    songs = fetch_songs(access_token)
    store_songs(songs)

if __name__ == '__main__':
    main()
