from tkinter import *


def sumbit():
    username = entry.get()
    print(f"wpisałes: {username}")
    print("test")
    #  entry.config(state=DISABLED)


def reset():
    entry.delete(0, END)


def backspace():
    entry.delete(len(entry.get()) - 1, END)


# Początek
window = Tk()
# head
window.title("Entrybox")

label = Label(window, text="Nauka entrybox", font=("Arial", 40))
label.pack(side=TOP)



# entrybox
entry = Entry(window, font=("Arial", 40),
              bg="black",
              fg="#00FF00")


entry.pack(side=LEFT)

#entry.insert(0, " spongebob")


# przycisk sumbit
sumbit_button = Button(window,
                       text="Sumbit",
                       command=sumbit,
                       width=10)

sumbit_button.pack(side=BOTTOM)

# przycisk reset
reset_button = Button(window,
                      text="Reset",
                      command=reset,
                      width=10)

reset_button.pack(side=BOTTOM)

# przycisk save
backspace_button = Button(window,
                          text="Backspace",
                          command=backspace,
                          width=10)

backspace_button.pack(side=BOTTOM)

window.mainloop()
# koniec
