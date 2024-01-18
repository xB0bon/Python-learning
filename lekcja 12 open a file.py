from tkinter import *
from tkinter import filedialog


def click():
    filepath = filedialog.askopenfilename(
        initialdir="C:\\Users\\Piotrek\\OneDrive - Zespół Szkół Technicznych im. Tadeusza Kościuszki w Radomiu\\Komputer domowy\\Desktop",
        title="Open file!",
        filetypes=(("Text files", "*.txt"),
                   ("All files", "*.*")))
    file = open(filepath, 'r')
    print(file.read())
    file.close()


window = Tk()
button = Button(window, text="file", command=click)
button.pack()
window.mainloop()
