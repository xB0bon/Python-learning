# -*- coding: utf-8 -*-
from tkinter import *
import math

def przycisk(num):
    global okno_tekst, ostatnia_operacja
    if num == "pierwiastek":
        try:
            wynik_pierwiastka = math.sqrt(float(okno_tekst))
            okno_tekst = str(wynik_pierwiastka)
            okno.set(okno_tekst)
        except ValueError:
            okno.set("Błędna wartość do obliczenia pierwiastka")
        return
    if ostatnia_operacja and num in ['/', '*', '+', '.', '-']:
        # Ignoruj kolejne kliknięcia tych samych operatorów
        return

    okno_tekst = okno_tekst + str(num)
    okno.set(okno_tekst)

    # Zapisz ostatnią operację tylko jeśli to jest operator
    if num in ['/', '*', '+', '.', '-']:
        ostatnia_operacja = num
    else:
        ostatnia_operacja = None


def clear(event=None):
    global okno_tekst
    okno.set("")
    okno_tekst = ""


def rowma():
    global okno_tekst
    try:
        total = str(eval(okno_tekst))
        okno.set(total)
        okno_tekst = total
    except ZeroDivisionError:
        okno.set("nie można dzielić przez 0!")
    except SyntaxError:
        okno.set("Znaki są wpisane niepoprawnie!")


window = Tk()

okno_tekst = ""

okno = StringVar()
ostatnia_operacja = None

label = Label(window, textvariable=okno, width=50, height=2, bg="black", fg="white")
label.pack()

frame = Frame(window)
frame.pack()
window.bind("<Escape>", clear)
button1 = Button(frame, text="1", command=lambda: przycisk(1), width=10, height=2, bg="gray", fg="white",
                 font=("arial", 10, "bold"))
button1.grid(row=0, column=0)

button2 = Button(frame, text="2", command=lambda: przycisk(2), width=10, height=2, bg="gray", fg="white",
                 font=("arial", 10, "bold"))
button2.grid(row=0, column=1)

button3 = Button(frame, text="3", command=lambda: przycisk(3), width=10, height=2, bg="gray", fg="white",
                 font=("arial", 10, "bold"))
button3.grid(row=0, column=2)

button4 = Button(frame, text="4", command=lambda: przycisk(4), width=10, height=2, bg="gray", fg="white",
                 font=("arial", 10, "bold"))
button4.grid(row=1, column=0)

button5 = Button(frame, text="5", command=lambda: przycisk(5), width=10, height=2, bg="gray", fg="white",
                 font=("arial", 10, "bold"))
button5.grid(row=1, column=1)

button6 = Button(frame, text="6", command=lambda: przycisk(6), width=10, height=2, bg="gray", fg="white",
                 font=("arial", 10, "bold"))
button6.grid(row=1, column=2)

button7 = Button(frame, text="7", command=lambda: przycisk(7), width=10, height=2, bg="gray", fg="white",
                 font=("arial", 10, "bold"))
button7.grid(row=2, column=0)

button8 = Button(frame, text="8", command=lambda: przycisk(8), width=10, height=2, bg="gray", fg="white",
                 font=("arial", 10, "bold"))
button8.grid(row=2, column=1)

button9 = Button(frame, text="9", command=lambda: przycisk(9), width=10, height=2, bg="gray", fg="white",
                 font=("arial", 10, "bold"))
button9.grid(row=2, column=2)

button0 = Button(frame, text="0", command=lambda: przycisk(0), width=10, height=2, bg="gray", fg="white",
                 font=("arial", 10, "bold"))
button0.grid(row=3, column=1)

button_dot = Button(frame, text=".", command=lambda: przycisk("."), width=10, height=2, bg="gray", fg="white",
                    font=("arial", 10, "bold"))
button_dot.grid(row=3, column=2)

button_podz = Button(frame, text="/", command=lambda: przycisk("/"), width=10, height=2, bg="gray", fg="white",
                     font=("arial", 10, "bold"))
button_podz.grid(row=0, column=3)

button_raz = Button(frame, text="*", command=lambda: przycisk("*"), width=10, height=2, bg="gray", fg="white",
                    font=("arial", 10, "bold"))
button_raz.grid(row=1, column=3)

button_minus = Button(frame, text="-", command=lambda: przycisk("-"), width=10, height=2, bg="gray", fg="white",
                      font=("arial", 10, "bold"))
button_minus.grid(row=2, column=3)

button_plus = Button(frame, text="+", command=lambda: przycisk("+"), width=10, height=2, bg="gray", fg="white",
                     font=("arial", 10, "bold"))
button_plus.grid(row=3, column=3)

button_rowna = Button(frame, text="=", command=rowma, width=10, height=2, bg="gray", fg="white",
                      font=("arial", 10, "bold"))
button_rowna.grid(row=4, column=3)

button_clear = Button(frame, text="clear", command=clear, width=10, height=2, bg="gray", fg="white",
                      font=("arial", 10, "bold"))
button_clear.grid(row=4, column=2)
button_pier = Button(frame, text="pierwiastek", command=lambda: przycisk("pierwiastek"), width=10, height=2, bg="gray", fg="white",
                      font=("arial", 10, "bold"))
button_pier.grid(row=5, column=0)
window.mainloop()


