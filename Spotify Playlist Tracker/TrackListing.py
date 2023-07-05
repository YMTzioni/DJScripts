import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

def get_playlist_ids_from_user():
    playlist_ids = []
    while True:
        playlist_id = input("Enter a playlist ID (or 'done' to finish): ")
        if playlist_id.lower() == 'done':
            break
        playlist_ids.append(playlist_id)
    return playlist_ids

def save_playlist_tracks_to_file(sp, playlist_id, file):
    results = sp.playlist(playlist_id)
    file.write(f"{results['name']}\n")
    for i, item in enumerate(results['tracks']['items']):
        track = item['track']
        file.write(f"{i+1}. {track['name']} by {track['artists'][0]['name']}\n")
    file.write("="*40 + "\n")

# Set up credentials
client_id = "your-client-id"
client_secret = "your-client-secret"

# Set up spotipy with your credentials
credentials = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=credentials)

# Get playlist IDs from the user
playlist_ids = get_playlist_ids_from_user()

# Save tracks from each playlist to the file
with open('playlists.txt', 'w') as file:
    for playlist_id in playlist_ids:
        save_playlist_tracks_to_file(sp, playlist_id, file)

print("Playlists successfully saved to playlists.txt.")
