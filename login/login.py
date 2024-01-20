import modules
from tkinter import *
from tkinter import messagebox

def login_new():
    def submit():
        username = entry1.get()
        password = entry2.get()

        if (username == 'Admin') and (password == 'admin'):
            if wybor.get() == 1:
                print(f"Zalogowano!\nWitaj {username}!")
                window.destroy()
                modules.okno()
            elif wybor.get() == 0:
                messagebox.showwarning("Uwaga", "Jeśli chcesz korzystać z programu, musisz zaakceptować regulamin.")
                print(f"Zaakceptuj regulamin, aby kontynuować!")
        else:
            print("Błąd!")

    def reset():
        entry1.delete(0, END)
        entry2.delete(0, END)

    def regulamin():
        if wybor.get() == 0:
            messagebox.showinfo("Uwaga", "Jeśli chcesz korzystać z programu, musisz zaakceptować regulamin.")

    window = Tk()
    window.title("Logowanie")
    window.geometry("320x300")
    window.maxsize(320, 300)
    window.configure(bg="#add8e6")

    main = Label(window, text="Zaloguj się:", font=("Arial", 30), bg="#add8e6")
    main.place(x=10, y=10)

    # username
    label = Label(window, text="Username:", font=("Arial", 15), bg="#add8e6")
    label.place(x=10, y=60)

    entry1 = Entry(window, font=("Arial", 20), bg="lightgrey", fg="black")
    entry1.place(x=10, y=90)

    # password
    label3 = Label(window, text="Password:", font=("Arial", 15), bg="#add8e6")
    label3.place(x=10, y=130)

    entry2 = Entry(window, font=("Arial", 20), bg="lightgrey", fg="black", show="*")
    entry2.place(x=10, y=170)

    wybor = IntVar()

    # checkbox
    checkbox1 = Checkbutton(window, text="Zgadzasz się z regulaminem", variable=wybor, onvalue=1, offvalue=0, command=regulamin, bg="#add8e6")
    checkbox1.place(x=10, y=210)

    # buttons
    # submit
    button = Button(window, text="Submit", font=("Arial", 15), command=submit, width=7, bg="#87ceeb")
    button.place(x=10, y=240)

    # reset
    button2 = Button(window, text="Reset", font=("Arial", 15), command=reset, width=7, bg="#87ceeb")
    button2.place(x=110, y=240)

    # exit
    button3 = Button(window, text="Exit", font=("Arial", 15), command=window.destroy, width=7, bg="#ff6666")
    button3.place(x=210, y=240)

    window.mainloop()
