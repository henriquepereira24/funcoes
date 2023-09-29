
lista = [27, 49, 68, 23, 82, 74, 14]


maior = lista[0]
casa = 0
casamaior = 0

for num in lista:
    if num > maior:
        maior = num
        casamaior = casa
    casa = casa+1

print (f'Numero:  {maior} Casa:{casamaior}')