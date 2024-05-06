# koszyk

class Koszyk:
    def __init__(self):
        self.lista = []
    def dodaj(self, wartosc):
        self.lista.append(wartosc)
    def koszt(self):
        x = 0
        for i in self.lista:
            x += i.zwroc_koszt()
        return x

    def produkty(self):
        for i in self.lista:
            print (i.__class__.__name__)
            i.wyswietl()

    def usun(self, id):
        self.lista.pop(id)

# parent class

class Towar:
    def __init__(self,marka, ilosc, cena):
        self.ilosc = ilosc
        self.cena = cena
        self.koszt = cena * ilosc
        self.marka = marka

    def zwroc_koszt(self):
        return self.koszt

    def zwroc_ilosc(self):
        return self.ilosc

    def zwroc_cena(self):
        return self.cena

    def wyswietl(self):
        print(f'marka: {self.marka}')
        print(f'ilosc: {self.ilosc}')
        print(f'cena: {self.cena}')
        print(f'koszt: {self.koszt}')
        print("")

## child class 

class rower(Towar):
    pass

rower1 = rower("cros", 1, 750)
rower2 = rower("gorski", 1, 1000)

class hulajnoga(Towar):
    pass

hulajnoga1 = hulajnoga("electric", 1, 500)
hulajnoga2 = hulajnoga("manual", 1, 150)

class pilka(Towar):
    pass

pilka1 = pilka("nozna", 2, 50)
pilka2 = pilka("siatkowa", 3, 40)

class buty(Towar):
    pass

buty1 = buty("adidas", 2, 200)
buty2 = buty("puma", 3, 150)

class namiot(Towar):
    pass

namiot1 = namiot("kechua", 1, 750)
namiot2 = namiot("alpina", 1, 960)

class krzeslo(Towar):
    pass

krzeslo1 = krzeslo("rozkladane", 5, 21)
krzeslo2 = krzeslo("sztywne", 3, 33)

# koszyki
koszyk1 = Koszyk()
koszyk2 = Koszyk()

koszyk1.dodaj(rower1)
koszyk1.dodaj(hulajnoga1)
koszyk1.dodaj(pilka1)
koszyk1.dodaj(buty1)
koszyk1.dodaj(namiot1)
koszyk1.dodaj(krzeslo1)

koszyk2.dodaj(rower2)
koszyk2.dodaj(hulajnoga2)
koszyk2.dodaj(pilka2)
koszyk2.dodaj(buty2)
koszyk2.dodaj(namiot2)
koszyk2.dodaj(krzeslo2)
# Opisy towarów i ich ilosc
print("==============KOSZYK1===================")
#koszyk1.produkty()
print(f'koszt koszyka1:{koszyk1.koszt()}')
print("")
print("==============KOSZYK2===================")
#koszyk2.produkty()
print(f'koszt koszyka2: {koszyk2.koszt()}')

# koszt towarow

a = 'Simple is better than complex'

a += 'Complex is better than complicated'

a = a.split()