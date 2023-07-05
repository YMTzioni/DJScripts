# Spotify Playlist Tracker

This folder contains scripts that interact with the Spotify API to fetch track listings from specified playlists and save them to a text file. Another script then takes this text file and generates an Excel file for easy access and organization.

## Scripts

1. `TrackListing.py`: Fetches track listings from user-specified Spotify playlists and saves them to `playlists.txt`.

2. `ExcelList.py`: Reads `playlists.txt` and converts it into an Excel file (`playlists.xlsx`), with each playlist as a separate sheet.

## How to Use

1. Ensure you have Python 3 installed on your system.

2. Install the required Python packages by running the following command in your terminal: pip install -r requirements.txt

3. Open the `TrackListing.py` script in a text editor.

4. Replace `'your-client-id'` in the script with your actual Spotify Client ID. To obtain a Spotify Client ID, create a Spotify Developer account and register a new application.

5. Run `TrackListing.py` and enter the Spotify playlist IDs for the playlists you want to track. Follow the prompts and enter `'done'` when finished.

6. Once the script completes, run `ExcelList.py` to convert the track listings into an Excel file.

Please refer to the comments within the scripts for more detailed information.


## License

This project is licensed under the MIT License - see the LICENSE.md file for details.
