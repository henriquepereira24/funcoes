letras = {}

frase = input(f'Insere uma frase: ')

for letra in frase:
    if letra in letras:
        letras[letra] += 1
    else:
        letras[letra] = 1

caracteres = []
for c in letras.keys():
    caracteres.append(c)
valores = []
for v in letras.values():
    valores.append(v)

print(caracteres)
print(valores)