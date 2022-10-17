import pygame
import tkinter as tkr
from tkinter.filedialog import askdirectory
import os

musicplayer = tkr.Tk()
musicplayer.title("MP3 Player")
musicplayer.geometry("450x350")

directory = askdirectory()
# chdir changes the current working directory to the specified path, takes argument as new directory path
os.chdir(directory)
songlist = os.listdir()
playlist = tkr.Listbox(musicplayer, font="Helvetica 12 bold",
                    bg="yellow", selectmode=tkr.SINGLE)

for item in songlist:
    pos = 0
    playlist.insert(pos, item)
    pos = pos + 1

# used for loading and playing sounds
pygame.init()
pygame.mixer.init()


def play():
    # controls streaming of audio and loads music file for playback
    pygame.mixer.music.load(playlist.get(tkr.ACTIVE))
    var.set(playlist.get(tkr.ACTIVE))
    # function that plays the music
    pygame.mixer.music.play()


def ExitMusicPlayer():
    pygame.mixer.music.stop()


def pause():
    pygame.mixer.music.pause()


def unpause():
    pygame.mixer.music.unpause()


PlayButton = tkr.Button(musicplayer, width=5, height=3, font="Helvetica 12 bold",
                        text="PLAY", command=play, bg="green", fg="white")
StopButton = tkr.Button(musicplayer, width=5, height=3, font="Helvetica 12 bold",
                        text="STOP", command=ExitMusicPlayer, bg="red", fg="white")
PauseButton = tkr.Button(musicplayer, width=5, height=3, font="Helvetica 12 bold",
                        text="PAUSE", command=pause, bg="blue", fg="white")
UnpauseButton = tkr.Button(musicplayer, width=5, height=3, font="Helvetica 12 bold",
                        text="UNPAUSE", command=unpause, bg="yellow", fg="black")

# used to monitor changes to tkinter variables
var = tkr.StringVar()
songtitle = tkr.Label(musicplayer, font="Helvetica 12 bold", textvariable=var)

songtitle.pack()
PlayButton.pack(fill="x")
StopButton.pack(fill="x")
PauseButton.pack(fill="x")
UnpauseButton.pack(fill="x")
playlist.pack(fill="both", expand="yes")

musicplayer.mainloop()
