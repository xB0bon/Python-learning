from tkinter import *

window = Tk()
window.minsize(width=450, height=230)
window.maxsize(width=450, height=230)

Label_info = Label(window, text="Enter your info:", font=("Arial", 20, "bold"))
Label_info.grid(row=0, column=0, columnspan=2)
# -----------------------------------------
Labelname = Label(window, text="First name: ", font=("Arial", 20), bg="red", width=9)
Labelname.grid(row=1, column=0)
# ******
Entryname = Entry(window, font=("Arial", 20), bg="lime")
Entryname.grid(row=1, column=1)
# -----------------------------------------
labellastname = Label(window, text="Last name: ", font=("Arial", 20), bg="red", width=9)
labellastname.grid(row=2, column=0)
# ******
Entrylastname = Entry(window, font=("Arial", 20), bg="lime")
Entrylastname.grid(row=2, column=1)
# -----------------------------------------
labelemail = Label(window, text="Email: ", font=("Arial", 20), bg="red", width=9)
labelemail.grid(row=3, column=0)
# ******
Entryemail = Entry(window, font=("Arial", 20), bg="lime")
Entryemail.grid(row=3, column=1)
# -----------------------------------------
button = Button(window, text="Sumbit", width=26, bg="blue", fg="white", font=("Arial", 20, "bold"))
button.grid(row=4, column=0, columnspan=2)

window.mainloop()