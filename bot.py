from pytube import YouTube
import tkinter as tk
from tkinter import filedialog

def download_video(url, save_path):
    try:
        # Create a YouTube object for the given URL
        yt = YouTube(url)
        
        # Filter streams to only include progressive MP4 files
        streams = yt.streams.filter(progressive=True, file_extension="mp4")
        
        # Get the highest resolution stream
        highest_res_stream = streams.get_highest_resolution()
        
        # Download the video to the specified output path
        highest_res_stream.download(output_path=save_path)
        
        print("Video downloaded!")
    except Exception as e:
        # Print any exceptions that occur during the download process
        print(e)
    

def open_file_dialog():
    # Open a dialog for selecting a directory and return the chosen folder path
    folder = filedialog.askdirectory()
    
    if folder:
        print(f"Selected Folder: {folder}")
    
    return folder

if __name__ == "__main__": 
    # Create and configure the Tkinter root window (main window)
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    
    # Prompt the user for a YouTube URL
    video_url = input("Please enter a YouTube URL: ")
    
    # Open a dialog to select the download location
    save_dir = open_file_dialog()

    if save_dir:
        # If a valid download location is selected, start the download
        print("Download starting...")
        download_video(video_url, save_dir)
    else:
        # If no download location is selected, print a message
        print("Invalid save location")
