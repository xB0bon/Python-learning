from tkinter import *


def clickreturn(event):
    print("you click ENTER")


def clickescape(event):
    print("you click ESCAPE!")


def clickedx(event):
    print("you click X!")


def clickedrandom(event):
    # print("you click key: " + str(event.keysym))

    if str(event.keysym) == "exclam":
        label.config(text="!")

    elif str(event.keysym) == "at":
        label.config(text="@")

    elif str(event.keysym) == "numbersign":
        label.config(text="#")

    elif str(event.keysym) == "dollar":
        label.config(text="$")

    elif str(event.keysym) == "percent":
        label.config(text="%")

    elif str(event.keysym) == "asciicircum":
        label.config(text="^")

    elif str(event.keysym) == "ampersand":
        label.config(text="&")

    elif str(event.keysym) == "asterisk":
        label.config(text="*")

    elif str(event.keysym) == "parenleft":
        label.config(text="(")

    elif str(event.keysym) == "parenright":
        label.config(text=")")

    else:
        label.config(text=str(event.keysym))


window = Tk()

window.bind("<Return>", clickreturn)
window.bind("<Escape>", clickescape)
window.bind("<x>", clickedx)
window.bind("<Key>", clickedrandom)

click = Label(window, font=("Arial", 50, "bold"), text="You click:")
click.pack()
label = Label(window, font=("Arial", 40, "bold"), padx=20, pady=20, text="enter something!")
label.pack()
window.mainloop()
