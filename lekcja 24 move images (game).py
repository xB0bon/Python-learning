from tkinter import *


def w_pressed(event):
    new_y = label.winfo_y() - 20
    if new_y >= 0:
        label.place(x=label.winfo_x(), y=new_y)


def s_pressed(event):
    new_y = label.winfo_y() + 20
    window_height = window.winfo_height()
    label_height = label.winfo_height()
    if new_y + label_height <= window_height:
        label.place(x=label.winfo_x(), y=new_y)


def a_pressed(event):
    new_x = label.winfo_x() - 20
    if new_x >= 0:
        label.place(x=new_x, y=label.winfo_y())


def d_pressed(event):
    new_x = label.winfo_x() + 20
    window_width = window.winfo_width()
    label_width = label.winfo_width()
    if new_x + label_width <= window_width:
        label.place(x=new_x, y=label.winfo_y())


window = Tk()
window.geometry("600x600")

label = Label(window, width=10, height=5, bg="red")
label.place(x=0, y=0)

# ----------w,s,a,d----------
# ---------------------------
window.bind("<w>", w_pressed)
# ---------------------------
window.bind("<s>", s_pressed)
# ---------------------------
window.bind("<d>", d_pressed)
# ---------------------------
window.bind("<a>", a_pressed)
# ---------------------------


# ---------strzałki----------
# ---------------------------
window.bind("<Up>", w_pressed)
# ---------------------------
window.bind("<Down>", s_pressed)
# ---------------------------
window.bind("<Right>", d_pressed)
# ---------------------------
window.bind("<Left>", a_pressed)
# ---------------------------

window.mainloop()
