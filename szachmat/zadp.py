plik = open('szachy.txt')
arr = [[0]*8]*8
wiersz = 0
kolumna = 0

for element in plik:
    while(wiersz<8):
        arr[wiersz][kolumna] = element
        wiersz= wiersz + 1
    kolumna = kolumna + 1
    wiersz = 0
#for li in arr:
 #   print(li)

for linia in plik:
    arr.append(linia)

for i in range(8):
    for j in range(8):
        print(arr[i][j])