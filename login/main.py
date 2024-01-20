import login
from tkinter import *

def login_screen():
    main.destroy()
    login.login_new()

def exit_program():
    main.destroy()

main = Tk()
main.geometry("400x300")
main.title("Aplikacja Logowania")
main.config(bg="#add8e6")

label1 = Label(main, text="Witaj!", font=("Consolas", 20), bg="#add8e6")
label1.pack(pady=20)

label2 = Label(main, text="Co chcesz zrobić?", font=("Consolas", 15), bg="#add8e6")
label2.pack(pady=10)

button1 = Button(main, text="Zaloguj się", command=login_screen, font=("Consolas", 12), bg="#87ceeb", padx=20, pady=10, width=12)
button1.pack()

button2 = Button(main, text="Wyjście", command=exit_program, font=("Consolas", 12), bg="#ff6666", padx=20, pady=10, width=12)
button2.pack()

main.mainloop()
