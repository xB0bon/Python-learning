from tkinter import *


def openFile():
    pass


def saveFile():
    pass


window = Tk()
window.title("menubar")
window.geometry("300x300")

menubar = Menu()
window.config(menu=menubar)
# -------------------------File-----------------------------
filemenu = Menu(menubar,
                tearoff=0,  # usuwana kreski
                )

menubar.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Open", command=openFile)
filemenu.add_command(label="Save", command=saveFile)
filemenu.add_separator()  # oddziela
filemenu.add_command(label="Exit", command=quit)

# ---------------------------Edit-------------------------------
editmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Edit", menu=editmenu)
editmenu.add_command(label="Copy")
editmenu.add_command(label="Paste")
editmenu.add_command(label="Cut")
editmenu.add_separator()
editmenu.add_command(label="Find")

window.mainloop()
