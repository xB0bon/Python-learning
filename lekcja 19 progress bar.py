from tkinter import *
from tkinter.ttk import *
import time
from tkinter import messagebox


def start():
    x = 0
    y = 100
    while x < y:
        bar['value'] += 1
        x += 1
        time.sleep(0.1)
        percent.set(str(round((x / y) * 100)) + "%")
        tasks.set(f"{x}/{y} GB downloaded!")
        window.update_idletasks()

        if x == 100:
            messagebox.showinfo(title='100%', message='100%')



window = Tk()
bar = Progressbar(length=500)
bar.pack()

percent = StringVar()
tasks = StringVar()
Label(window, textvariable=percent).pack()
Label(window, textvariable=tasks).pack()
Button(window, text="DOWNLOAD", command=start).pack()
window.mainloop()
