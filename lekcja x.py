x = input("Jak masz na imię?: ")
zn = True
print(f"Witaj {x}!")

z = input(f"Co chcesz napisać?: ")
while True:
    try:
        y = int(input(f"Ile razy chcesz napisać {z}?: "))
        if y > 30000:
            print("Trochę za dużo!")
        else:
            break


    except ValueError:
        print("Wpisz liczbę!")
        

for i in range(1, y + 1):
    print(f"{i}.{z}.")

