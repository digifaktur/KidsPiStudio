# Kids Pi Studio
# A small audio recording studio for my children
# GNU GPL v2
# Created 2022 by Florian

# MediaPlayer.py
# Simple UI for audacious / audtool
 
import subprocess
from tkinter import *


class MediaPlayer(Frame):
    def __init__(self, master=None, path=None):
        subprocess.call(['killall', 'audacious'])
        self.playMediaWindow = Toplevel(master)
        self.playMediaWindow.geometry("720x320")
        self.playMediaWindow.title("KidsPiStudio - Media Player")
        self.playMediaWindow.protocol("WM_DELETE_WINDOW", self.closeWindow)
        self.currentWindow = self.playMediaWindow
        self.playimage = PhotoImage(file='./assets/play.png')
        self.pauseimage = PhotoImage(file='./assets/pause.png')
        self.stopimage = PhotoImage(file='./assets/stop.png')
        self.previmage = PhotoImage(file='./assets/prev.png')
        self.nextimage = PhotoImage(file='./assets/next.png')
        self.closeimage=PhotoImage(file='./assets/close.png')
        subprocess.Popen(['audacious', '-H', path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        mediaPlayButton = Button(self.playMediaWindow, image=self.playimage, width=160, command=subprocess.call(['audtool', '--playback-play']))
        mediaPlayButton.place(x=10, y=10)
        mediaPauseButton = Button(self.playMediaWindow, image=self.pauseimage, width=160, command=subprocess.call(['audtool', '--playback-pause']))
        mediaPauseButton.place(x=180, y=10)
        mediaStopButton = Button(self.playMediaWindow, image=self.stopimage, width=160, command=subprocess.call(['audtool', '--playback-stop']))
        mediaStopButton.place(x=350, y=10)
        mediaPrevButton = Button(self.playMediaWindow, image=self.previmage, width=160, command=subprocess.call(['audtool', '--playlist-advance']))
        mediaPrevButton.place(x=10, y=160)
        mediaNextButton = Button(self.playMediaWindow, image=self.nextimage, width=160, command=subprocess.call(['audtool', '--playlist-reverse']))
        mediaNextButton.place(x=180, y=160)
        closeButton = Button(self.playMediaWindow, image=self.closeimage, width=160, command=self.closeWindow)
        closeButton.place(x=520, y=160)
    def closeWindow(self):
        subprocess.call(['killall', 'audacious'])
        self.playMediaWindow.destroy()