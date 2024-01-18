import modules
from tkinter import *
from tkinter import messagebox


def sumbit():
    username = entry1.get()
    password = entry2.get()

    if (username == 'Admin') and (password == 'admin'):
        if wybor.get() == 1:
            print(f"Zalogowano!\nWitaj {username}!")
            window.destroy()
            modules.main()



        elif wybor.get() == 0:
            messagebox.showwarning("Uwaga", "Jeśli chcesz korzystać z programu musisz zaakceptować regulamin.")
            print(f"Zaakceptuj regulamin aby kontynuować!")
    else:
        print("błąd!")


def reset():
    entry1.delete(0, END)
    entry2.delete(0, END)


def regulamin():
    if wybor.get() == 0:
        messagebox.showinfo("Uwaga", "Jeśli chcesz korzystać z programu musisz zaakceptować regulamin.")


window = Tk()
window.title("Logowanie")
window.geometry("320x300")
window.maxsize(320, 300)
main = Label(window,
             text="Zaloguj się:",
             font=("Arial", 30))
main.place(x=10, y=10)

#  username
label = Label(window,
              text="Username:",
              font=("Arial", 15))
label.place(x=10, y=60)

entry1 = Entry(window,
               font=("Arial", 20),
               bg="grey",
               fg="black")
entry1.place(x=10, y=90)

#  password
label3 = Label(window,
               text="Password::",
               font=("Arial", 15))
label3.place(x=10, y=130)

entry2 = Entry(window, font=("Arial", 20),
               bg="grey",
               fg="black",
               show="*")
entry2.place(x=10, y=170)

wybor = IntVar()

#  chekbox
checkbox1 = Checkbutton(window,
                        text="Zgadzasz się z regulaminem",
                        variable=wybor,
                        onvalue=1,
                        offvalue=0,
                        command=regulamin)

checkbox1.place(x=10, y=210)

# buttoms
#  sumbit
button = Button(window,
                text="Sumbit",
                font=("Arial", 15),
                command=sumbit)

button.place(x=10, y=240)

#  reset
button2 = Button(window,
                 text="Reset",
                 font=("Arial", 15),
                 command=reset)
button2.place(x=100, y=240)

window.mainloop()
