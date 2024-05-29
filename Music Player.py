import tkinter as tk
from tkinter import filedialog, messagebox, Listbox
from pygame import mixer
import os

class MusicPlayer(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Music Player")
        self.geometry("500x400")
        self.configure(bg="lightblue")

        mixer.init()

        self.playlist = []
        self.current_song_index = 0

        self.create_widgets()

    def create_widgets(self):
        self.add_button = tk.Button(self, text="Add Song", command=self.add_song, bg="white", fg="black")
        self.add_button.pack(pady=10)

        self.play_button = tk.Button(self, text="Play", command=self.play_song, bg="green", fg="white")
        self.play_button.pack(pady=10)

        self.stop_button = tk.Button(self, text="Stop", command=self.stop_song, bg="red", fg="white")
        self.stop_button.pack(pady=10)

        self.pause_button = tk.Button(self, text="Pause", command=self.pause_song, bg="yellow", fg="black")
        self.pause_button.pack(pady=10)

        self.resume_button = tk.Button(self, text="Resume", command=self.resume_song, bg="yellow", fg="black")
        self.resume_button.pack(pady=10)

        self.playlist_box = Listbox(self, bg="white", fg="black", selectbackground="gray", selectforeground="white")
        self.playlist_box.pack(pady=10, fill=tk.BOTH, expand=True)
        
        self.bind("<Double-1>", self.play_selected_song)

    def add_song(self):
        song_path = filedialog.askopenfilename(filetypes=[("MP3 Files", "*.mp3")])
        if song_path:
            self.playlist.append(song_path)
            song_name = os.path.basename(song_path)
            self.playlist_box.insert(tk.END, song_name)

    def play_song(self):
        if self.playlist:
            song_path = self.playlist[self.current_song_index]
            mixer.music.load(song_path)
            mixer.music.play()
            song_name = os.path.basename(song_path)
            self.title(f"Playing - {song_name}")
        else:
            messagebox.showerror("Error", "Playlist is empty! Add songs to play.")

    def stop_song(self):
        mixer.music.stop()
        self.title("Music Player")

    def pause_song(self):
        mixer.music.pause()

    def resume_song(self):
        mixer.music.unpause()

    def play_selected_song(self, event):
        try:
            selected_index = self.playlist_box.curselection()[0]
            self.current_song_index = selected_index
            self.play_song()
        except IndexError:
            messagebox.showerror("Error", "Please select a song to play.")

    def on_closing(self):
        mixer.music.stop()
        self.destroy()

if __name__ == "__main__":
    app = MusicPlayer()
    app.protocol("WM_DELETE_WINDOW", app.on_closing)
    app.mainloop()
