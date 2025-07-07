#Egy függvényt tesztelünk, amely bekér egy sztringet szóközökkel (min 1) és a bekért sztringből kiveszi a szóközöket.

def without_space():
    text = input("Write a short text!").split()
    print(f"Your text without spaces is: {''.join(text)}")

without_space()
