from tkinter import *
from tkinter import filedialog


def save():
    file = filedialog.asksaveasfile(defaultextension='.txt',
                                    filetypes=[("Text Files", ".txt"),
                                               ("HTML files", ".html"),
                                               ("Python Files", "*.py"),
                                               ("All Files", "*.*")],
                                    initialdir="C:\\Users\\Piotrek\\OneDrive - Zespół Szkół Technicznych im. Tadeusza Kościuszki w Radomiu\\Komputer domowy\\Desktop")

    filetext = str(textarea.get(1.0, END))
    file.write(filetext)
    file.close()


window = Tk()
button = Button(window, text="save", command=save)
button.pack()
textarea = Text(window,
                height=8,
                width=20,
                font=("Arial", 20),
                bg="light yellow"
                )
textarea.pack()
window.mainloop()
