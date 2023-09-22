
list = [10, 8, 80, 49, 20, 41, 20, 25, 34, 27, 100]

# imprimir elementos da lista e dizer se é par ou impar

for x in list:
    if x % 2 == 0:
        print(f'o numero {x} é par')

    else:
        print(f'o numero {x} é impar')

# tem


for z in range(len(list)):
    if list[z] % 2 == 0:
        print(list[z], 'é par')
    else:
        print(list[z], 'é impar')



