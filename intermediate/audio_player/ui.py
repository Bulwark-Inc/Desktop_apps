import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from logic import AudioPlayer
from mutagen.mp3 import MP3
from PIL import Image, ImageTk

class AudioPlayerUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Audio Player")
        self.root.geometry("500x300")
        self.root.resizable(True, True)

        self.player = AudioPlayer()

        # Song Metadata
        self.song_label = tk.Label(root, text="No song loaded", font=("Arial", 12))
        self.song_label.pack(pady=5)

        # Progress Bar
        self.progress = ttk.Scale(root, from_=0, to=100, orient="horizontal", command=self.seek_track)
        self.progress.pack(fill="x", padx=20, pady=5)

        # Controls
        button_frame = tk.Frame(root)
        button_frame.pack(pady=10)

        self.prev_button = tk.Button(button_frame, text="⏮", command=self.prev_track)
        self.prev_button.grid(row=0, column=0, padx=5)

        self.play_button = tk.Button(button_frame, text="▶", command=self.toggle_play)
        self.play_button.grid(row=0, column=1, padx=5)

        self.next_button = tk.Button(button_frame, text="⏭", command=self.next_track)
        self.next_button.grid(row=0, column=2, padx=5)

        # Volume Control
        self.volume_icon = tk.Button(root, text="🔊", command=self.toggle_volume)
        self.volume_icon.pack(side="left", padx=10)
        self.volume_slider = ttk.Scale(root, from_=0, to=100, orient="vertical", command=self.change_volume)
        self.volume_slider.pack(side="left")
        self.volume_slider.pack_forget()

        # File Selection
        self.load_button = tk.Button(root, text="Load Song", command=self.load_song)
        self.load_button.pack(pady=10)

    def toggle_play(self):
        self.player.play_pause()
        self.play_button.config(text="⏸" if self.player.is_playing else "▶")

    def prev_track(self):
        pass  # Implement Previous Track Logic

    def next_track(self):
        pass  # Implement Next Track Logic

    def change_volume(self, volume):
        self.player.set_volume(float(volume) / 100)

    def toggle_volume(self):
        if self.volume_slider.winfo_ismapped():
            self.volume_slider.pack_forget()
        else:
            self.volume_slider.pack(side="left")

    def load_song(self):
        file_path = filedialog.askopenfilename(filetypes=[("MP3 Files", "*.mp3")])
        if file_path:
            self.player.load(file_path)
            self.display_metadata(file_path)

    def display_metadata(self, file_path):
        audio = MP3(file_path)
        duration = int(audio.info.length)
        self.progress.config(to=duration)
        self.song_label.config(text=file_path.split("/")[-1])

    def seek_track(self, position):
        self.player.seek(int(float(position)))

