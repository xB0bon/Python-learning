from tkinter import *

food = ["pizza", "kebab", "fries", "hamburger"]

window = Tk()

x = IntVar()

pizzaimage = PhotoImage(file="like2.png")
KEBABimage = PhotoImage(file="z2.png")
FRIESimage = PhotoImage(file="like2.png")
hamburgerimage = PhotoImage(file="z2.png")

images = [pizzaimage, KEBABimage, FRIESimage, hamburgerimage]


for index in range(len(food)):
    RadioButton = Radiobutton(window,
                              text=food[index],
                              value=index,
                              variable=x,
                              font=("Arial", 20, "bold"),
                              image=images[index],
                              compound=RIGHT,
                              indicatoron=0,# usuwa kropki
                              width=775)
    RadioButton.pack(anchor=W)

window.mainloop()
