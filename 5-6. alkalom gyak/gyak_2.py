

tanulok = [ { "nev": "Teszt Elek", "osztaly": "13I", "eletkor": 19 }, { "nev": "Kiss Béla", "osztaly": "12A",
"eletkor": 18 }, { "nev": "Nagy Anna", "osztaly": "11B", "eletkor": 17 }, { "nev": "Szabó Gergő", "osztaly": "10C",
"eletkor": 16 }, { "nev": "Varga László", "osztaly": "9D", "eletkor": 15 }, { "nev": "Tóth Zsófia", "osztaly": "12A",
"eletkor": 18 } ]

def kiiratas():
    print("A jelenlegi tanulók:")
    for tanulo in tanulok:
        print(f"{tanulo['nev']} {tanulo['eletkor']} éves és a {tanulo['osztaly']} osztályba jár.")

def uj_tanulo():
    nev = input("Név: ")
    eletkor = int(input("Életkor: "))
    osztaly = input("Osztály: ")
    tanulok.append({"nev": nev, "eletkor": eletkor, "osztaly": osztaly})
    print(f"{nev} hozzáadva ({osztaly}).")

def torles():
    nev = input("Mi a neve a tanulónak? ")
    megerosites = input("Biztos, hogy törölni akarja? (I/N): ")
    if megerosites.lower() == "i":
        for tanulo in tanulok:
            if tanulo["nev"] == nev:
                tanulok.remove(tanulo)
                print(f"{nev} törlésre került.")
                return
            
def modositas():
    nev = input("Mi a tanuló neve? ")
    kulcs = input("Módosítandó adat: ")
    uj_ertek = input("Új adat: ")
    for tanulo in tanulok:
        if tanulo["nev"] == nev:
            tanulo[kulcs] = int(uj_ertek) if kulcs == "eletkor" else uj_ertek
            print(f"{kulcs} módosításra került.")
            return

def listazas():
    vege_szavak = ["q", "end", "quit"]
    valasz = ""
    while valasz not in vege_szavak:
        kiiratas()
        print("\n Új tag - newmem | Törlés - delete | Módosítás - modify | Kilépés - end, Q, quit")
        valasz = input("Mit szeretnél csinálni? ").lower()

        if valasz == "newmem":
            uj_tanulo()
        elif valasz == "delete":
            torles()
        elif valasz == "modify":
            modositas()
        elif valasz not in vege_szavak:
            print("Nem megadott utasítás.")
listazas()
