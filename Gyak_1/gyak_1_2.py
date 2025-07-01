#Egy függvényt tesztelünk, amely két szám közül adja vissza a kisebb dupláját.
#Írj egy függvényt "kisebb_dupla" néven, amely két számot kap paraméterül és visszaadja a kisebb szám dupláját.

def smaller_double(a, b):
    try:
        a = float(a)
        b = float(b)
        if a.is_integer():
            a = int(a)
        if b.is_integer():
            b = int(b)
        if a != b:
            smaller = min(a,b)
            print(f"Your numbers are {a} and {b}. \n Double of the smaller one is {round(smaller * 2, 2)}")
        else:
            print(f"Your numbers are {a} and {b}. \n These are equal.")
    except ValueError:
        print("These are not numbers!")

smaller_double(2.1, 3.0)
