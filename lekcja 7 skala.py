from tkinter import *
def sumbit():
    print(f"The temperature is {scale.get()} degrees Celsius.")

window = Tk()
window.title("Skala")

scale = Scale(window,
              from_=100, to=-50,
              length=600,
              orient=VERTICAL,
              font=("Consolas", 20),
              tickinterval= 10,# NUMERY PO BOKU
              #resolution=5 # zmienianie  co 5
              troughcolor="aqua",
              fg="red"

              )
scale.pack()

button = Button(window, text="Sumbit", command=sumbit)
button.pack()
window.mainloop()
