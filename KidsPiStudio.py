from tkinter import *

class MainWindow(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.pack(fill=BOTH, expand=1)
        self.cdimage=PhotoImage(file='./assets/cd2.png')
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
        closeButton = Button(discWindow, image=self.closeimage, width=160, command=discWindow.destroy)
        closeButton.place(x=520, y=160)
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