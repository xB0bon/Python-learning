# -*- coding: utf-8 -*-
from tkinter import *


def func1(event):
    print(f"Mouse coordinates: {event.x}, {event.y}")


window = Tk()

window.bind('<Button-1>', func1)

# window.bind('<Button-1>', func1) # lewy przycisk
# window.bind('<Button-2>', func1) # wciskanie scroll
# window.bind('<Button-3>', func1) # prawy przycisk
# window.bind('<ButtonRelease>', func1) # Każdy przycisk
# window.bind('<Enter>', func1) # po najechaniu myszką
# window.bind('<Leave>', func1) # po opuszczeniu okienka
# window.bind('<Motion>', func1) # gdy myszka się rusza


window.mainloop()
