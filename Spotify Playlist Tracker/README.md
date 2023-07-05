# Spotify Playlist Tracker

This folder contains scripts that interact with the Spotify API to fetch track listings from specified playlists and save them to a text file. Another script then takes this text file and generates an Excel file for easy access and organization.

## Scripts

1. `track_listing.py`: Fetches track listings from user-specified Spotify playlists and saves them to `playlists.txt`.

2. `playlist_to_excel.py`: Reads `playlists.txt` and converts it into an Excel file (`playlists.xlsx`), with each playlist as a separate sheet.

## How to Use

1. Make sure you have Python 3 installed on your system.

2. Install the required Python packages by running `pip install -r requirements.txt` in your terminal.

3. Run `python track_listing.py` and enter the Spotify playlist IDs for the playlists you want to track.

4. After the script completes, run `python playlist_to_excel.py` to convert the track listings into an Excel file.

Refer to the comments in the scripts for more detailed information.

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.
