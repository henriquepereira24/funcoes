listanumeros = [300, 54, 15]

maior = listanumeros[0]
menor = listanumeros[0]

for x in listanumeros:
    if x > maior:
        maior = x
    else:
        if x < menor:
            menor = x

print(f'Dos 3 numeros listados, o número {maior}, é o maior da lista.')
print(f'Dos 3 numeros listados, o número {menor}, é o menor da lista.')