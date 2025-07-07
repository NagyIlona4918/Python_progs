#Egy függvényt tesztelünk, amely két szám szorzatát adja vissza eredményül.
#Írj egy függvényt "szorzat" néven, amely két számot vár paraméterül és visszaadja a szorzatukat.
#Ha nem számot adnak meg, fusson hibára!

def product(a, b):
    try:
        a = float(a)
        b = float(b)
        if a.is_integer():
            a = int(a)
        if b.is_integer():
            b = int(b)
        print(f"Your numbers are {a} and {b}. \n The product of them is {round(a * b, 2)}")
    except ValueError:
        print(f"These are not numbers!")

product(2.1, 3.0)
