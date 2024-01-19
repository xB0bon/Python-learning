from tkinter import *

window = Tk()
frame = Frame(window,
              bg="pink",
              bd=5,
              relief=RAISED
              )
frame.pack()

Button(frame, text="W", width=3, font=("Arial", 20)).pack(side=TOP)
Button(frame, text="A", width=3, font=("Arial", 20)).pack(side=LEFT)
Button(frame, text="S", width=3, font=("Arial", 20)).pack(side=LEFT)
Button(frame, text="D", width=3, font=("Arial", 20)).pack(side=LEFT)
window.mainloop()