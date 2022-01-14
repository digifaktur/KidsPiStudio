# Kids Pi Studio
# A small audio recording studio for my children
# GNU GPL v2
# Created 2022 by Florian

# MediaPlayer.py
# Simple UI for audacious / audtool
 
from email.mime import base
import subprocess
from tkinter import *


class MediaPlayer(Frame):
    def __init__(self, master=None, path=None):
        playMediaWindow = Toplevel(master)
        playMediaWindow.geometry("720x320")
        playMediaWindow.title("KidsPiStudio - Media Player")
        self.playimage = PhotoImage(file='./assets/play.png')
        self.pauseimage = PhotoImage(file='./assets/pause.png')
        self.stopimage = PhotoImage(file='./assets/stop.png')
        self.previmage = PhotoImage(file='./assets/prev.png')
        self.nextimage = PhotoImage(file='./assets/next.png')
        self.closeimage=PhotoImage(file='./assets/close.png')
        subprocess.Popen(['audacious', '-H', path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        mediaPlayButton = Button(playMediaWindow, image=self.playimage, width=160, command=lambda : subprocess.call(['audtool', '--playback-play']))
        mediaPlayButton.place(x=10, y=10)
        mediaPauseButton = Button(playMediaWindow, image=self.pauseimage, width=160, command=lambda : subprocess.call(['audtool', '--playback-pause']))
        mediaPauseButton.place(x=180, y=10)
        mediaStopButton = Button(playMediaWindow, image=self.stopimage, width=160, command=lambda : subprocess.call(['audtool', '--playback-stop']))
        mediaStopButton.place(x=350, y=10)
        mediaPrevButton = Button(playMediaWindow, image=self.previmage, width=160, command=lambda : subprocess.call(['audtool', '--playlist-advance']))
        mediaPrevButton.place(x=10, y=160)
        mediaNextButton = Button(playMediaWindow, image=self.nextimage, width=160, command=lambda : subprocess.call(['audtool', '--playlist-reverse']))
        mediaNextButton.place(x=180, y=160)
        closeButton = Button(playMediaWindow, image=self.closeimage, width=160, command=playMediaWindow.destroy)
        closeButton.place(x=520, y=160)
