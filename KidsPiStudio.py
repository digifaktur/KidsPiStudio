import subprocess
from tkinter import *
from subprocess import Popen, PIPE
from functools import partial

class MainWindow(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.pack(fill=BOTH, expand=1)
        self.currentWindow = master
        self.playimage = PhotoImage(file='./assets/play.png')
        self.pauseimage = PhotoImage(file='./assets/pause.png')
        self.stopimage = PhotoImage(file='./assets/stop.png')
        self.previmage = PhotoImage(file='./assets/prev.png')
        self.nextimage = PhotoImage(file='./assets/next.png')
        self.cdimage=PhotoImage(file='./assets/cd2.png')
        self.playcdimage=PhotoImage(file='./assets/playCd.png')
        self.ripcdimage=PhotoImage(file='./assets/ripCd.png')
        self.notesimage=PhotoImage(file='./assets/notes.png')
        self.recordimage=PhotoImage(file='./assets/record.png')
        self.exitimage=PhotoImage(file='./assets/exit.png')
        self.closeimage=PhotoImage(file='./assets/close.png')
        discButton = Button(self, image=self.cdimage, width=160, command=self.clickDiscButton)
        discButton.place(x=10, y=10)
        notesButton = Button(self, image=self.notesimage, width=160, command=self.clickNotesButton)
        notesButton.place(x=10, y=160)
        recordButton = Button(self, image=self.recordimage, width=160, command=self.clickRecordButton)
        recordButton.place(x=180, y=10)
        exitButton = Button(self, image=self.exitimage, width=160, command=self.clickExitButton)
        exitButton.place(x=520, y=160)
    def clickDiscButton(self):
        discWindow = Toplevel(self)
        discWindow.geometry("720x320")
        discWindow.title("KidsPiStudio - CD Studio")
        playDiscButton = Button(discWindow, image=self.playcdimage, width=160, command=self.clickPlayMediaButton)
        playDiscButton.place(x=10, y=10)
        ripDiscButton = Button(discWindow, image=self.ripcdimage, width=160, command=self.clickRipDiscButton)
        ripDiscButton.place(x=10, y=160)
        closeButton = Button(discWindow, image=self.closeimage, width=160, command=discWindow.destroy)
        closeButton.place(x=520, y=160)
    def clickPlayMediaButton(self):
        playMediaWindow = Toplevel(self)
        playMediaWindow.geometry("720x320")
        playMediaWindow.title("KidsPiStudio - Media Player")
        self.currentWindow = playMediaWindow
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
    def clickRipDiscButton(self):
        return
    def clickNotesButton(self):
        notesWindow = Toplevel(self)
        notesWindow.geometry("720x320")
        notesWindow.title("KidsPiStudio - MP3 Studio")
        closeButton = Button(notesWindow, image=self.closeimage, width=160, command=notesWindow.destroy)
        closeButton.place(x=520, y=160)
    def clickRecordButton(self):
        recordWindow = Toplevel(self)
        recordWindow.geometry("720x320")
        recordWindow.title("KidsPiStudio - Recording Studio")
        closeButton = Button(recordWindow, image=self.closeimage, width=160, command=recordWindow.destroy)
        closeButton.place(x=520, y=160)
    def clickExitButton(self):
        exit()



root = Tk()
app = MainWindow(root)
root.wm_title("KidsPiStudio")
root.geometry("720x320")
root.mainloop()