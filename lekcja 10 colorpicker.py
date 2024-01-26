from tkinter import *
from tkinter import colorchooser


def click():
    result = colorchooser.askcolor()[1]
    window.config(bg=result)


window = Tk()
window.geometry("400x400")
window.title("colorpicker")

buttom1 = Button(window, command=click, text="Click me!")
buttom1.pack()
window.mainloop()
