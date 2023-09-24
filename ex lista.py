
# Crie duas lista de números inteiros
lista1 = [1, 2, 3, 4, 5, 6, 7]
lista2 = [10, 20, 30, 40, 50, 60, 70]

soma = 0

for i in range(len(lista1)):
    soma += lista1[i] + lista2[i]

print (soma)

# encontre e fazer print o maior numero entre as duas listas
maior = lista1[0]
for i in range(len(lista1)):
    if lista2[i] > maior:
        maior = lista2[i]

print (maior)

# encontre o menor numero entre as duas listas
menor = lista1[0]
for i in range(len(lista1)):
    if lista2[i] < menor:
        menor = lista2[i]

print (menor)










