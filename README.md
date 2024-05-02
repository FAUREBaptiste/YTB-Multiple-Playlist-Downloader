# YouTube Playlist Downloader

This project is a Python-based application designed to download audio from YouTube playlists and store them in specified directories. The application features a graphical user interface (GUI) built with `tkinter`,
allowing users to enter multiple playlist URLs, choose an output folder, and start the download process with ease.

## Features
- Download audio from multiple YouTube playlists
- Save audio files in separate subfolders named after the playlist
- Easy-to-use GUI for simple interaction
- Output in `bestaudio` format without additional conversion

## Installation
To use this application, download the executable file from the provided link or location. No additional Python setup is required, as the executable is self-contained.
OR copy past the script and use it in your IDE (Do not forget to install the needed packages).

### System Requirements
- Windows 10 or later
- Enough storage space to store downloaded audio files

## Usage
1. Launch the application by double-clicking the executable file.
2. Enter one or more YouTube playlist URLs, each on a new line.
3. Click "Choose Output Folder" to select where to save the audio files.
4. Click "Download" to start downloading audio from the specified playlists.
5. Once the download is complete, check the selected output folder for the downloaded audio files.
![GUI](https://github.com/FAUREBaptiste/YTB-Multiple-Playlist-Downloader/assets/168738566/b3e17b20-09e2-4263-ae93-78c209897254)


## Troubleshooting
### Security Warnings
If you encounter a security warning when running the application, follow these steps:
1. Right-click on the executable file and select "Properties."
2. If there's a checkbox labeled "Unblock," check it and click "OK."
3. If using Windows SmartScreen, click "More info" and then "Run anyway."
4. If the executable is blocked by antivirus software, add it to the antivirus's exception or allowlist.

### Application Not Working
If the application does not work as expected, ensure the following:
- You have a stable internet connection.
- The YouTube playlist URLs are correct and publicly accessible.
- You have sufficient permissions to write to the output folder.

## License
[GNU GENERAL PUBLIC LICENSE]

## Acknowledgements
- This project uses `yt_dlp` and `pytube` for downloading YouTube content.
- `tkinter` is used for the graphical user interface.
  
