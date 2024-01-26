from tkinter import *


def newwindow():
    window2 = Toplevel()  # będzie wyświetlac się nad innymi okienkami


window = Tk()
window.title("new windows")

Button(window, text="Create new window", command=newwindow).pack()
window.mainloop()
