#Egy függvényt tesztelünk, amely egy egész szám alapján kiírja, hogy az páratlan-e.
#Írj egy függvényt "paros_paratlan" néven, amely a bejövő paraméter alapján kiírja, hogy az páros-e vagy páratlan. Pl. így: Ez a szám ... páros.

def odd_even(a):
    try:
        a = float(a)
        if a.is_integer():
            a = int(a)
            if a % 2 == 0:
                print(f"Your number {a} is even.")
            else:
                print(f"Your number {a} is odd.")
        else:
            print(f"The number {a} is not an integer!")
    except ValueError:
        print(f"The {a} is not an integer!")
    
odd_even(2.0)
