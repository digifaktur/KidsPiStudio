import subprocess
from tkinter import *


class MediaPlayer(Frame):
    def __init__(self, master=None, path=None):
        subprocess.call(['killall', 'audacious'])
        playMediaWindow = Toplevel(master)
        playMediaWindow.geometry("720x320")
        playMediaWindow.title("KidsPiStudio - Media Player")
        playMediaWindow.protocol("WM_DELETE_WINDOW", self.closeWindow)
        self.currentWindow = playMediaWindow
        self.playimage = PhotoImage(file='./assets/play.png')
        self.pauseimage = PhotoImage(file='./assets/pause.png')
        self.stopimage = PhotoImage(file='./assets/stop.png')
        self.previmage = PhotoImage(file='./assets/prev.png')
        self.nextimage = PhotoImage(file='./assets/next.png')
        subprocess.Popen(['audacious', '-H', path], creationflags=subprocess.DETACHED_PROCESS, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        #time.sleep(3)
        #subprocess.call(['audtool', '--playlist-addurl', path])
        mediaPlayButton = Button(playMediaWindow, image=self.playimage, width=160, command=subprocess.call(['audtool', '--playback-play']))
        mediaPlayButton.place(x=10, y=10)
        mediaPauseButton = Button(playMediaWindow, image=self.pauseimage, width=160, command=subprocess.call(['audtool', '--playback-pause']))
        mediaPauseButton.place(x=180, y=10)
        mediaStopButton = Button(playMediaWindow, image=self.stopimage, width=160, command=subprocess.call(['audtool', '--playback-stop']))
        mediaStopButton.place(x=350, y=10)
        mediaPrevButton = Button(playMediaWindow, image=self.previmage, width=160, command=subprocess.call(['audtool', '--playlist-advance']))
        mediaPrevButton.place(x=10, y=160)
        mediaNextButton = Button(playMediaWindow, image=self.nextimage, width=160, command=subprocess.call(['audtool', '--playlist-reverse']))
        mediaNextButton.place(x=180, y=160)
        closeButton = Button(playMediaWindow, image=self.closeimage, width=160, command=self.closeWindow)
        closeButton.place(x=520, y=160)
    def closeWindow(self):
        subprocess.call(['audtool', '--shutdown'])
        self.currentWindow.destroy()