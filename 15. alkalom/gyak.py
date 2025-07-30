class Ember:
    def __init__(self, nev, eletkor):
        self.nev = nev
        self.eletkor = eletkor

    def bemutatkozik(self):
        print(f'{self.nev} vagyok, {self.eletkor} éves.')

class Tanar(Ember):
    def __init__(self, nev, eletkor, tantargy):
        super().__init__(nev, eletkor)
        self.tantargy = tantargy
        self.osztaly = ""

    def osztalyt_kap(self, osztaly):
        self.osztaly = osztaly

    def bemutatkozik(self):
        print(f'{self.nev} vagyok, {self.eletkor} éves, {self.tantargy}-t tanítok a(z) {self.osztaly} osztályban.')

class Diak(Ember):
    def __init__(self, nev, eletkor):
        super().__init__(nev, eletkor)
        self.osztaly = ""
        self.osztalyzatok = []

    def add_grade(self, grade):
        self.osztalyzatok.append(grade)

    def average(self):
        return sum(self.osztalyzatok) / len(self.osztalyzatok) if self.osztalyzatok else 0

    def set_osztaly(self, osztaly):
        self.osztaly = osztaly

    def bemutatkozik(self):
        print(f'{self.nev} vagyok, {self.eletkor} éves, a(z) {self.osztaly} osztályba járok. {self.osztalyzatok} jegyeim vannak, az átlagom: {self.average():.2f}')

class Osztaly:
    def __init__(self, nev):
        self.nev = nev
        self.tanarok = []
        self.diakok = []

    def add_tanar(self, tanar):
        self.tanarok.append(tanar)

    def add_diak(self, diak):
        self.diakok.append(diak)

    def osztaly_info(self):
        print(f'Osztály: {self.nev}')
        for tanar in self.tanarok:
            tanar.bemutatkozik()
        for diak in self.diakok:
            diak.bemutatkozik()

osztaly = Osztaly("12.A")
tanar = Tanar("Kovács Péter", 40, "Matematika")
tanar.osztalyt_kap("12.A")
osztaly.add_tanar(tanar)

diak_a = Diak("Nagy Antal", 16)
diak_a.set_osztaly("12.A")
diak_a.add_grade(4)
diak_a.add_grade(5)
diak_a.add_grade(2)
osztaly.add_diak(diak_a)

diak_b = Diak("Kiss Anna", 15)
diak_b.set_osztaly("12.A")
diak_b.add_grade(5)
diak_b.add_grade(3)
diak_b.add_grade(4)
osztaly.add_diak(diak_b)

diak_c = Diak("Kékesi Lilla", 14)
diak_c.set_osztaly("12.A")
diak_c.add_grade(5)
diak_c.add_grade(5)
diak_c.add_grade(5)
osztaly.add_diak(diak_c)

osztaly.osztaly_info()