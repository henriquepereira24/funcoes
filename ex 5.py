
list = [10, 8, 80, 49, 20, 41, 20, 25, 34, 27, 100]

# imprime o numero de casas na lista
print(len(list))

# imprime a sequencia de numeros entre 0 e o numero de casas na lista menos um

for x in range(len(list)):
    print(x)

# imprime a sequencia de numeros entre numero de casas da lista menos um e zero. usa a variavel y
print()
numero = len(list) - 1
for y in range(len(list)):
    print(numero)
    numero = numero - 1

# imprime a lista na ordem inversa
print()
inverso = len(list) - 1
for z in range(len(list)):
    print(f'{inverso} = {list[z]}')
    inverso = inverso -1

#outro exemplo
print()
numero = len(list) - 1
for y in range(len(list)):
    print(list[numero])
    numero = numero - 1
