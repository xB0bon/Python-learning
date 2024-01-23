from tkinter import *
import keyboard 


def sumbit():
    food = []

    for i in listbox.curselection():
        food.insert(i, listbox.get(i))
    print("You ordered:")
    for i in food:
        print(i)


def add():
    listbox.insert(listbox.size(), entry.get())  # listbox.size() - daje na koniec listy
    listbox.config(height=listbox.size())  # dopasowanie


def delete():
    for i in reversed(listbox.curselection()):
        listbox.delete(i)
        listbox.config(height=listbox.size())


window = Tk()
window.title("listbox")

listbox = Listbox(window,
                  bg="#f7ffde",
                  font=("Arial", 35),
                  width=12,
                  selectmode="multiple"
                  )
listbox.pack()

listbox.insert(1, "pizza")
listbox.insert(2, "kebab")
listbox.insert(3, "spagetti")
listbox.insert(4, "hamburger")
listbox.insert(5, "sausage")

listbox.config(height=listbox.size())  # dopasowanie

entry = Entry(window)
entry.pack()


add = Button(window, text="add", command=add)
add.pack()

sumbit = Button(window, text="sumbit", command=sumbit)
sumbit.pack()

delete = Button(window, text="delete", command=delete)
delete.pack()

window.mainloop()
