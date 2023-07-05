import pandas as pd
import re

# Parse the playlist file
playlists = {}
with open('playlists.txt', 'r') as file:
    current_playlist = None
    for line in file:
        line = line.strip()
        if not line:
            continue
        if line.startswith("="*40):  # We've reached the end of a playlist
            current_playlist = None
        elif current_playlist is None:  # We're at the start of a new playlist
            current_playlist = line
            playlists[current_playlist] = []
        else:  # We're reading a song from the current playlist
            _, rest = line.split('. ', 1)
            song_title, artist = re.search('(.*) by (.*)', rest).groups()
            playlists[current_playlist].append([song_title, artist])

# Convert the playlists into an Excel file
with pd.ExcelWriter('playlists.xlsx') as writer:
    for playlist, songs in playlists.items():
        df = pd.DataFrame(songs, columns=["Song Title", "Artist"])
        df.to_excel(writer, sheet_name=playlist[:30])  # sheet_name must be <= 31 characters long

print("Playlists successfully saved to playlists.xlsx.")
