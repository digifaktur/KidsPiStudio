from tkinter import *

class MainWindow(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.pack(fill=BOTH, expand=1)
        discButton = Button(self, image=PhotoImage("assets/cd2.png"), height=80, width=80, command=self.clickDiscButton)
        discButton.place(x=10, y=10)
    def clickDiscButton(self):
        exit()


root = Tk()
app = MainWindow(root)

root.wm_title("KidsPiStudio")
root.geometry("720x320")
root.mainloop()

