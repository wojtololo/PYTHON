
class Sprzet:

    def __init__(self, identyfikator, typ):
        self.__identyfikator = identyfikator
        self.__typ = typ

    def zwroc_ID(self):
        return self.__identyfikator

    def zwroc_typ(self):
        return self.__typ

    def wypisz(self):
        print('identyfikator: ' , self.__identyfikator)
        print('identyfikator: ' + self.typ)

class Osoba:
    def __init__(self, identyfikator, nazwisko, wiek):
        self.__identyfikator = identyfikator
        self.__nazwisko = nazwisko
        self.__wiek = wiek

    def zwroc_ID(self):
        return self.__identyfikator

    def zwroc_nazwisko(self):
        return self.__nazwisko

    def zwroc_wiek(self):
        return self.__wiek

    def wypisz(self):
        print('\nidentyfikator' ,self.__identyfikator)
        print('nazwisko: ' ,self.__nazwisko)
        print('wiek: ' ,self.__wiek)

class Wypozyczenie:
    def __init__(self, identyfikator_S, identyfikator_O):
        self.__identyfikator_S = identyfikator_S
        self.__identyfikator_O = identyfikator_O

    def zwroc_ID_S(self):
        return self.__identyfikator_S

    def zwroc_ID_O(self):
        return self.__identyfikator_O

    def wypisz(self):
        print('identyfikator Sprzetu: ' , self.__identyfikator_S)
        print('identyfikator Osoby: ' , self.__identyfikator_O)

def zad1(tab_s, tab_o, tab_w):
    tab = []
    for x in tab_o:
        if x.zwroc_wiek() > 25:
            for y in tab_s:
                if y.zwroc_typ() == 'hulajnoga':
                    for z in tab_w:
                        if z.zwroc_ID_S() == y.zwroc_ID() and z.zwroc_ID_O() == x.zwroc_ID():
                            tab.append(x)
    return tab

def zad2(tab_s, tab_w):
    suma = 0
    for i in tab_s:
        if i.zwroc_typ() == 'rower':
            for j in tab_w:
                if i.zwroc_ID() == j.zwroc_ID_S():
                    suma+=1
    return suma

tab_s = [
    Sprzet('S1', 'rower'),
	Sprzet('S2', 'hulajnoga'),
	Sprzet('S3', 'rolki'),
	Sprzet('S4', 'rower'),
	Sprzet('S5', 'hulajnoga'),
	Sprzet('S6', 'rolki')
    ]
tab_o = [
    Osoba('O1', 'Kowalski', 26),
	Osoba('O2', 'Nowak', 28),
	Osoba('O3', 'Mazur', 29),
	Osoba('O4', 'Wisniewski', 30),
	Osoba('O5', 'Wojcik', 35),
	Osoba('O6', 'Lewandowski', 40)
    ]
tab_w = [
    Wypozyczenie('S6', 'O5'),
	Wypozyczenie('S1', 'O6'),
	Wypozyczenie('S2', 'O1'),
	Wypozyczenie('S3', 'O2'),
	Wypozyczenie('S4', 'O3'),
	Wypozyczenie('S5', 'O4') 
    ]

##zad1
print('\nLista hulajnog wypozyczonych przez osoby starsze niz 25 lat: ')
lista = zad1(tab_s, tab_o, tab_w)
for i in lista:
    i.wypisz()
##zad2
print('\nliczba wypozyczonych rowerow: ', zad2(tab_s, tab_w))