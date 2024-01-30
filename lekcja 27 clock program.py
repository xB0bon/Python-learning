from tkinter import *
import time


def update():
    day_now = time.strftime("%A")
    day_label.config(text=day_now)

    date_now = time.strftime("%d %B, %Y")
    date_label.config(text=date_now)

    time_now = time.strftime("%H:%M:%S")
    time_label.config(text=time_now)

    window.after(1000, update)


window = Tk()
window.title("Zegar")
window.minsize(width=300, height=180)
window.maxsize(width=300, height=180)
day_label = Label(window, text="", fg="#ff6600", font=("Arial", 30, "bold"))
day_label.pack()

time_label = Label(window, text="", fg="#00ff00", bg="black", font=("Arial", 40, "bold"))
time_label.pack()

date_label = Label(window, fg="#3366cc", font=("Arial", 20, "bold"))
date_label.pack()

update()
window.mainloop()
