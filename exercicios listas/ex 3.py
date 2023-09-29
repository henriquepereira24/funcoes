

lista = [10, 20, 15, 5, 60, 140, 80, 40]
print(lista)

# se o valor do elemento da lista é >=20, então o valor do elemento da lista é dividido por 2

#[10, 20, 10, 7.5, 5, 30, 70, 40, 20]

# numb = 0
#
# for num in lista:
#     if num >= 20:
#         lista[numb] = num / 2
#     numb = numb + 1

#print(lista)

# Outro exemplo

for x in range(len(lista)):
    if lista[x] >= 20:
        lista[x] = lista[x] / 2
print(lista)



