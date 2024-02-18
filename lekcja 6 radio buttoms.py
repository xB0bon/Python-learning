from tkinter import *

food = ["pizza", "kebab", "fries", "hamburger"]

window = Tk()

x = IntVar()





for index in range(len(food)):
    RadioButton = Radiobutton(window,
                              text=food[index],
                              value=index,
                              variable=x,
                              font=("Arial", 20, "bold"),
                              compound=RIGHT,
                              # usuwa kropki
                              width=775)
    RadioButton.pack(anchor=W)

window.mainloop()
