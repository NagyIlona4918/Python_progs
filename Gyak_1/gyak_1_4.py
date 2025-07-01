#Egy függvényt tesztelünk, amely két szám közül adja vissza a nagyobb háromszorosát.
#Írj függvényt "nagyobbTripla" néven, amely visszaadja a két szám közül a nagyobb háromszorosát.

def largerTriple(a, b):
    try:
        a = float(a)
        b = float(b)
        if a.is_integer():
            a = int(a)
        if b.is_integer():
            b = int(b)
        if a != b:
            larger = max(a,b)
            print(f"Your numbers are {a} and {b}. \n Triple of the larger one is {round(larger * 3, 2)}")
        else:
            print(f"Your numbers are {a} and {b}. \n These are equal.")
    except ValueError:
        print("These are not numbers!")

largerTriple(2.1, 3.0)
