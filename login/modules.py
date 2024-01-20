from tkinter import *
import login

def uruchom_kalkulator():
    # Tutaj dodaj kod do uruchamiania kalkulatora
    print("Uruchomiono kalkulator")

def uruchom_inna_aplikacje():
    # Tutaj dodaj kod do uruchamiania innej aplikacji
    print("Uruchomiono inną aplikację")

def okno():
    window1 = Tk()
    window1.title("Program")
    window1.geometry("800x600")

    label1 = Label(window1, text="Witaj!\nZ jakiej aplikacji chcesz skorzystać?", font=("Arial", 20))
    label1.pack(pady=20)

    frame1 = Frame(window1, bg="aquamarine", bd=5, relief=GROOVE)
    frame1.pack(pady=20)


    photo_kalkulator = PhotoImage(file="like2.png")
    button1 = Button(frame1,
                     text="Uruchom kalkulator",
                     image=photo_kalkulator
                     , compound=TOP,
                     command=uruchom_kalkulator,
                     font=("Arial", 15),
                     padx=20,
                     pady=10,
                     bg="#87ceeb")
    button1.pack(side=LEFT, padx=20)

    photo_inna_aplikacja = PhotoImage(file="like2.png")  # Zmień obrazek na odpowiedni
    button2 = Button(frame1,
                     text="inna aplikacja",
                     image=photo_inna_aplikacja
                     , compound=TOP,
                     command=uruchom_inna_aplikacje,
                     font=("Arial", 15),
                     padx=20,
                     pady=10,
                     bg="#87ceeb")
    button2.pack(side=LEFT, padx=20)

    window1.mainloop()

okno()
