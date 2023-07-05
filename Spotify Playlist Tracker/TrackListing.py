import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

def save_playlist_tracks_to_file(sp, playlist_id, file):
    # Get the playlist
    results = sp.playlist(playlist_id)
    playlist_name = results['name']

    # Write the playlist name to the file
    file.write(f"{playlist_name}\n")

    # Write the tracks to the file
    for i, item in enumerate(results['tracks']['items']):
        track = item['track']
        file.write(f"{i+1}. {track['name']} by {track['artists'][0]['name']}\n")

    # Write a separating line
    file.write("\n" + "="*40 + "\n\n")

# Set up credentials
client_id = "30666c46e5424ea1843860af9f7f5bae"
client_secret = "420f661e71094781b82577d0975b6617"

# Set up spotipy with your credentials
credentials = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=credentials)

# IDs for the playlists you want to track
playlist_ids = ['6tDBMuvQIjN3Hw1FFQAWJV', '37i9dQZF1DWVCHIm2MEeIy', '0Naxntr7EFcJuUZnFklQN3', '2otQLmbi8QWHjDfq3eL0DC', '37i9dQZF1EQpoj8u9Hn81e', '4RlWgU7BtMfU4Y3Jf5noGd', '1QuIG2NU4mLvxjc04jKKMj', '7jd0DWWFBt7PGFQfaJF9x7', '2bv09sNb6nHH63oBxTq0Wc', '37i9dQZF1DXa8NOEUWPn9W']

# Open the output file
with open("playlists.txt", 'w') as file:
    # Save tracks from each playlist to the file
    for playlist_id in playlist_ids:
        save_playlist_tracks_to_file(sp, playlist_id, file)
