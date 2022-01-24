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
        self.mediaPlayer = None
        self.buttonCount = 0
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
        self.createButtons(notesWindow, self.buttonCount)
        navButton = Button(notesWindow, image=self.arrowimage, width=150, command=lambda : self.createButtons(notesWindow))
        navButton.place(x=520, y=10)
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
    def clickExitButton(self):
        exit()
    def createButtons(self, wnd):
        cnt = 0
        for currentdir, subdirs, files in os.walk('~/Music'):
            for dirname in subdirs:
                if cnt < self.buttonCount:
                    cnt += 1
                    continue
                jpath = os.path.join(currentdir, dirname, 'cover.jpg')
                ppath = os.path.join(currentdir, dirname, 'cover.png')
                icon = self.notesimage
                if os.path.exists(jpath) and not os.path.exists(ppath):
                    cover = Image.open(jpath)
                    w, h = cover.size
                    if w > 140:
                        ratio = (140, h * (140 / w))
                        cover = cover.resize(ratio)
                        cover.save(ppath)
                if os.path.exists(ppath):
                    icon = PhotoImage(file=ppath)
                tmpButton = Button(wnd, image=icon, width=160, command=lambda : self.clickPlayMediaButton(os.path.join(currentdir, dirname)))
                tmpButton.place(x=10 + ((self.buttonCount % 4) // 2) * 170, y=10 + (self.buttonCount % 2) * 150)
                self.buttonCount += 1
                if self.buttonCount % 4 == 0:
                    break
            if self.buttonCount % 4 == 0:
                break


root = Tk()
app = MainWindow(root)
root.wm_title("KidsPiStudio")
root.geometry("720x320")
root.mainloop()