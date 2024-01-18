from tkinter import *


def sumbit():
    input = text.get(1.0, END)
    print(input)


window = Tk()

text = Text(window, font=("Ink Free", 25), width=20, height=8, bg="light yellow", fg="black", padx=20, pady=20)
text.pack()

buttom = Button(window, text="sumbit", command=sumbit)
buttom.pack()

window.mainloop()
