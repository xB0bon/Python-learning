from tkinter import *
from tkinter import messagebox


def agree():
    if x.get() == 1:
        print("You agreed")
    else:
        print("You don't agree")
        messagebox.showinfo("Warning!", "You have to agree, if you want to use program!")


window = Tk()
x = IntVar()


checkbox1 = Checkbutton(window,
                        text="I agree to something",
                        variable=x,
                        onvalue=1,
                        offvalue=0,
                        command=agree,
                        compound=LEFT)

checkbox1.pack()
window.mainloop()
