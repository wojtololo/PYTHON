
def znajdz(plik):
    slownik = {
        1:0,
        2:0,
        3:0,
        4:0,
        5:0,
        6:0,
        7:0,
        8:0,
        9:0
    }
    f = open(plik, "rt")
    #wpisanie do s³ownika ile razy dana cyfra wyst¹pi³a
    for linia in f:
        x = int(linia[0])
        y = slownik.get(x) + 1
        slownik.update({x: y})

    f.close()

    suma = 0
    for cyfra in slownik:
        suma += slownik[cyfra]

    for cyfra in slownik:
        print(f'Cyfra: {cyfra}')
        print(f'Wystapila: {slownik[cyfra]} razy')
        proc = round(float(slownik[cyfra]/suma)*100, 2)
        print(f'Stanowi ona: {proc} % wszystkich pierwszych cyfr')
        print("")

print("Ludnosc Miast z Unii Europejskiej")
znajdz("LudnoscEuropy.txt")

print("Powierzchnia wyzej wymienionych miast")
znajdz("PowierzchniaEuropy.txt")

print("Ludnosc Miast z Azji")
znajdz("LudnoscAzji.txt")

print("Powierzchnia wyzej wymienionych miast")
znajdz("PowierzchniaAzji.txt")

print("Najdlozsze rzeki swiata")
znajdz("Rzeki.txt")