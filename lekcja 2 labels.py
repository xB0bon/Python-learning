from tkinter import *

window = Tk()
window.title("Labels pozdro pozdro")
window.geometry("400x400")
print("siema")
photo = PhotoImage(file="z2.png")
label = Label(window, text="hello world!",
              font=("Arial", 40, "bold"),
              fg="#00ff00", bg="black",
              relief=RAISED, bd=10,
              padx=60,
              pady=30,
              image=photo, compound="bottom")
# label.pack() # wyswietla na środku
#label.place(x=0, y=0)
label.pack()

window.mainloop()
