# -*- coding: utf-8 -*-
"""
Created on Wed May  1 20:26:17 2024

@author: S7471
"""
import os
import tkinter as tk
from tkinter import filedialog
import yt_dlp
from pytube import Playlist


# Function to get playlist information (name and URLs)
def get_playlist_info(playlist_url):
    pl = Playlist(playlist_url)
    return pl.title, [url for url in pl]


# Function to download audio from YouTube videos into a specified folder
def download_audio(video_url, output_folder):
    ydl_opts = {
        'format': 'bestaudio',  # Best available audio quality without conversion
        'outtmpl': os.path.join(output_folder, '%(title)s.%(ext)s'),  # Save with the original extension
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])


# Create a simple tkinter GUI
root = tk.Tk()
root.title("YouTube Playlist Downloader")

# Function to select output folder
def choose_output_folder():
    folder = filedialog.askdirectory()
    output_folder_var.set(folder)


# Function to download audio from multiple playlist URLs
def download_from_playlists():
    base_output_folder = output_folder_var.get()  # Get base output folder
    
    if not base_output_folder:
        status_var.set("Please choose an output folder.")
        return
    
    playlist_urls = playlist_text.get("1.0", "end-1c").strip()  # Get playlist URLs from Text widget
    
    if not playlist_urls:
        status_var.set("Please provide playlist URLs.")
        return
    
    # Split playlist URLs by newlines to get a list of URLs
    playlist_urls_list = playlist_urls.split('\n')

    for playlist_url in playlist_urls_list:
        if not playlist_url.strip():
            continue  # Skip empty lines
        
        playlist_name, urls = get_playlist_info(playlist_url.strip())  # Get playlist info

        # Create subfolder for the playlist
        subfolder = os.path.join(base_output_folder, playlist_name)
        os.makedirs(subfolder, exist_ok=True)

        # Download audio for this playlist
        for url in urls:
            download_audio(url.strip(), subfolder)

    status_var.set(f"Downloaded audio files to '{base_output_folder}'.")
    

# Variables for the GUI
output_folder_var = tk.StringVar()
status_var = tk.StringVar()

# GUI layout
tk.Label(root, text="YouTube Playlist URLs (one per line):").pack(pady=10)
playlist_text = tk.Text(root, height=10, width=50, wrap='word')  # Multi-line input
playlist_text.pack()  # Note that Text doesn't support textvariable

tk.Button(root, text="Choose Output Folder", command=choose_output_folder).pack(pady=10)
tk.Label(root, textvariable=output_folder_var).pack()

tk.Button(root, text="Download", command=download_from_playlists).pack(pady=10)

tk.Label(root, textvariable=status_var).pack(pady=10)

root.mainloop()  # Start the GUI event loop
