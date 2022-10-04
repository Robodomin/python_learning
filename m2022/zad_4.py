plik = open('liczby.txt')
for linia in plik:
    linia = linia.strip()
    # print(linia)
    liniaOdr = linia[::-1]
    # print(liniaOdr)
    liczba = int(linia)
    # print(liczba)
    if(liczba %17 == 0):
        print(liczba)

    zawartosc = plik.readline()
    # print(zawartosc)