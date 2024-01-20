from tkinter import *

count = 0


def click1():
    global count
    count += 1
    print(f"Kliknąłeś like {count} raz")


window = Tk()
window.title("buttons")
label = Label(window,
              text="Click me!",
              font=("Arial", 40, "bold"),
              fg="#00ff00",
              bg="black")
label.pack()
photo = PhotoImage(file="login/like2.png")
button1 = Button(window,
                 text="click me!",
                 font=("Arial", 20, "bold"),
                 fg="red",
                 bg="white",
                 state=ACTIVE,
                 command=click1, image=photo)
button1.pack()
window.mainloop()
