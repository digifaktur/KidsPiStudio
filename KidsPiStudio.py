# Kids Pi Studio
# A small audio recording studio for my children
# GNU GPL v2
# Created 2022 by Florian

# KidsPiStudio.py
# General UI

import os
import datetime
import subprocess
from time import sleep
from tkinter import *
from MediaPlayer import MediaPlayer
from Album import Album

class MainWindow(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.pack(fill=BOTH, expand=1)
        self.currentWindow = master
        self.cdimage=PhotoImage(file='./assets/cd2.png')
        self.playcdimage=PhotoImage(file='./assets/playCd.png')
        self.ripcdimage=PhotoImage(file='./assets/ripCd.png')
        self.notesimage=PhotoImage(file='./assets/notes.png')
        self.recordimage=PhotoImage(file='./assets/record.png')
        self.exitimage=PhotoImage(file='./assets/exit.png')
        self.closeimage=PhotoImage(file='./assets/close.png')
        self.arrowleftimage=PhotoImage(file='./assets/prev.png')
        self.arrowrightimage=PhotoImage(file='./assets/next.png')
        self.mediaPlayer = None
        self.buttonCount = 0
        self.albums = []
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
        playDiscButton = Button(discWindow, image=self.playcdimage, width=160, command=self.clickPlayMediaButton("cdda://"))
        playDiscButton.place(x=10, y=10)
        ripDiscButton = Button(discWindow, image=self.ripcdimage, width=160, command=self.clickRipDiscButton)
        ripDiscButton.place(x=10, y=160)
        closeButton = Button(discWindow, image=self.closeimage, width=160, command=discWindow.destroy)
        closeButton.place(x=520, y=160)
    def clickPlayMediaButton(self, path):
        self.mediaPlayer = MediaPlayer(self, path)
    def clickRipDiscButton(self):
        rip = subprocess.Popen(["abcde", "-G", "-N"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    def clickNotesButton(self):
        notesWindow = Toplevel(self)
        notesWindow.geometry("720x320")
        notesWindow.title("KidsPiStudio - MP3 Studio")
        self.albums.clear()
        a1Button = None;
        a2Button = None;
        a3Button = None;
        a4Button = None;
        for dirname in [f.path for f in os.scandir(os.path.join(os.path.expanduser('~'), 'Music')) if f.is_dir()]:
            self.albums.append(Album(dirname))
        if (len(self.albums) > 0):
            a1Button = Button(notesWindow, image=self.albums[self.buttonCount].albumicon, width=150, command=lambda : self.clickPlayMediaButton(self.albums[self.buttonCount].albumpath))
            a1Button.place(x=10, y=10)
            if (len(self.albums) > 1):
                a2Button = Button(notesWindow, image=self.albums[self.buttonCount + 1].albumicon, width=150, command=lambda : self.clickPlayMediaButton(self.albums[self.buttonCount + 1].albumpath))
                a2Button.place(x=180, y=10)
                if (len(self.albums) > 2):
                    a3Button = Button(notesWindow, image=self.albums[self.buttonCount + 2].albumicon, width=150, command=lambda : self.clickPlayMediaButton(self.albums[self.buttonCount + 2].albumpath))
                    a3Button.place(x=350, y=10)
                    if (len(self.albums) > 3):
                        a4Button = Button(notesWindow, image=self.albums[self.buttonCount + 3].albumicon, width=150, command=lambda : self.clickPlayMediaButton(self.albums[self.buttonCount + 3].albumpath))
                        a4Button.place(x=520, y=10)
        navButtonleft = Button(notesWindow, image=self.arrowleftimage, width=150, command=lambda : self.navigate(4, a1Button, a2Button, a3Button, a4Button))
        navButtonleft.place(x=10, y=160)
        navButtonright = Button(notesWindow, image=self.arrowrightimage, width=150, command=lambda : self.navigate(-4, a1Button, a2Button, a3Button, a4Button))
        navButtonright.place(x=180, y=160)
        closeButton = Button(notesWindow, image=self.closeimage, width=160, command=notesWindow.destroy)
        closeButton.place(x=520, y=160)
    def clickRecordButton(self):
        recordWindow = Toplevel(self)
        recordWindow.geometry("720x320")
        recordWindow.title("KidsPiStudio - Recording Studio")
        tenSecondsButton = Button(recordWindow, text='10 s', font=('Helvetica bold', 36), fg='green', command=lambda : self.recordAudio(10))
        tenSecondsButton.place(x=10, y=10)
        twentySecondsButton = Button(recordWindow, text='20 s', font=('Helvetica bold', 36), fg='green', command=lambda : self.recordAudio(20))
        twentySecondsButton.place(x=10, y=160)
        thirtySecondsButton = Button(recordWindow, text='30 s', font=('Helvetica bold', 36), fg='green', command=lambda : self.recordAudio(30))
        thirtySecondsButton.place(x=180, y=10)
        oneMinuteButton = Button(recordWindow, text='1 min', font=('Helvetica bold', 36), fg='green', command=lambda : self.recordAudio(60))
        oneMinuteButton.place(x=180, y=160)
        threeMinutesButton = Button(recordWindow, text='3 min', font=('Helvetica bold', 36), fg='green', command=lambda : self.recordAudio(180))
        threeMinutesButton.place(x=350, y=10)
        closeButton = Button(recordWindow, image=self.closeimage, width=160, command=recordWindow.destroy)
        closeButton.place(x=520, y=160)
    def recordAudio(self, length):
        countdownWindow = Toplevel(self)
        countdownWindow.geometry("720x320")
        countdownWindow.title("KidsPiStudio - Audio Recording")
        countdownWindow.config(bg='skyblue4')
        timeLabel = Label(countdownWindow, font=('Helvetica bold', 72), text='-3', bg='skyblue4', fg='red')
        timeLabel.place(x=260, y=70)
        countdownWindow.wait_visibility()
        date_time = datetime.datetime.now().strftime('%Y%m%d_%H-%M-%S')
        wavpath = '/home/pi/Music/Recordings/' + date_time + '.wav'
        seconds = -3
        while seconds < 0:
            timeLabel.config(text=str(seconds))
            countdownWindow.update()
            sleep(1)
            seconds += 1
        subprocess.Popen(['arecord', wavpath, '-D', 'sysdefault:CARD=1', '-f', 'cd', '-d', str(length)], stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        timeLabel.config(text='0', fg='chartreuse2')
        while seconds < length:
            timeLabel.config(text=str(seconds))
            countdownWindow.update()
            sleep(1)
            seconds += 1
        self.clickPlayMediaButton(wavpath)
        countdownWindow.destroy()
    def navigate(self, cnt, b1 : Button, b2 : Button, b3 : Button, b4 : Button):
        self.buttonCount += cnt
        if self.buttonCount < 0 or self.buttonCount > (len(self.albums) - cnt):
            self.buttonCount = len(self.albums) - abs(cnt)
        if isinstance(b1, Button):
            b1.config(image=self.albums[self.buttonCount].albumicon)
            b1.config(command=lambda : self.clickPlayMediaButton(self.albums[self.buttonCount].albumpath))
            if isinstance(b2, Button):
                b2.config(image=self.albums[self.buttonCount + 1].albumicon)
                b2.config(command=lambda : self.clickPlayMediaButton(self.albums[self.buttonCount + 1].albumpath))
                if isinstance(b3, Button):
                    b3.config(image=self.albums[self.buttonCount + 2].albumicon)
                    b3.config(command=lambda : self.clickPlayMediaButton(self.albums[self.buttonCount + 2].albumpath))
                    if isinstance(b4, Button):
                        b4.config(image=self.albums[self.buttonCount + 3].albumicon)
                        b4.config(command=lambda : self.clickPlayMediaButton(self.albums[self.buttonCount + 3].albumpath))
    def clickExitButton(self):
        exit()
        
        


root = Tk()
app = MainWindow(root)
root.wm_title("KidsPiStudio")
root.geometry("720x320")
root.mainloop()
