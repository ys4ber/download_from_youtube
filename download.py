from tkinter import *
from pytube import YouTube
from pytube.exceptions import AgeRestrictedError

def download():
    video_url = url.get()
    youtube = YouTube(video_url, on_progress_callback=progress)
    try:
        video = youtube.streams.get_highest_resolution()
        video.download()
        status.set("Download completed")
    except AgeRestrictedError:
        login()

def progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage = (bytes_downloaded / total_size) * 100
    status.set(f"Downloading... {percentage:.2f}%")

def login():
    login_window = Toplevel(root)
    login_window.geometry("300x150")
    login_window.title("YouTube Login")

    Label(login_window, text="Enter your YouTube login credentials:").grid(row=0, column=0, padx=10, pady=10)
    Label(login_window, text="Email:").grid(row=1, column=0, padx=10, pady=5)
    email_entry = Entry(login_window, width=30)
    email_entry.grid(row=1, column=1, padx=10, pady=5)

    Label(login_window, text="Password:").grid(row=2, column=0, padx=10, pady=5)
    password_entry = Entry(login_window, width=30, show="*")
    password_entry.grid(row=2, column=1, padx=10, pady=5)

    Button(login_window, text="Login", command=lambda: authenticate(email_entry.get(), password_entry.get(), login_window)).grid(row=3, column=1, padx=10, pady=10)

def authenticate(email, password, login_window):
    youtube = YouTube()
    youtube.login(email, password)
    login_window.destroy()
    download()

root = Tk()
root.geometry("500x150")
root.title("YouTube Video Downloader")

url = StringVar()
status = StringVar()
status.set("Enter the URL of the YouTube video to download")

Label(root, text="Enter URL:").grid(row=0, column=0, padx=10, pady=10)
Entry(root, width=60, textvariable=url).grid(row=0, column=1, padx=10, pady=10)
Label(root, textvariable=status).grid(row=1, column=1, padx=10, pady=10)
Button(root, text="Download", command=download).grid(row=2, column=1, padx=10, pady=10)

root.mainloop()

