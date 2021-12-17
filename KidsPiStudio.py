from tkinter import *

class MainWindow(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.pack(fill=BOTH, expand=1)
        self.cdimage=PhotoImage(file='./assets/cd2.png')
        discButton = Button(self, image=self.cdimage, command=self.clickDiscButton)
        discButton.place(x=10, y=10)
    def clickDiscButton(self):
        exit()


root = Tk()
app = MainWindow(root)
root.wm_title("KidsPiStudio")
root.geometry("720x320")
root.mainloop()

