from tkinter import *
from tkinter import messagebox
def hello():
    while True:
        messagebox.showinfo("Virus", "You have a VIRUS!!!")

window = Tk()
window.title("siema")
button = Button(window, command=hello, text="CLICK ME!")
button.pack()
window.mainloop()