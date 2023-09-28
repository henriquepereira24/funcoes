vendas = [

        # Gasolina
        [
           # OR CT OC
            [1, 2, 3],    # Verão
            [4, 5, 6],    # Outono
            [7, 8, 9],    # Inverno
            [10, 11, 12]  # Primavera
        ],
        # Gasóleo
        [
           # OR CT OC
            [13, 14, 15],  # Verão
            [16, 17, 18],  # Outono
            [19, 20, 21],  # Inverno
            [22, 23, 24]   # Primavera
        ]

]


#print(f'Comprimento da Lista Vendas:{len(vendas)}')


print('.............X Y Z.............')
total1 = 0
for x in range(len(vendas)):
    total2 = 0
    for  y in range(len(vendas[0])):
        total3 = 0
        for z in range(len(vendas[0][0])):
            total1 += vendas[x][y][z]
            total2 += vendas[x][y][z]
            total3 += vendas[x][y][z]
        print(f'total3 : {total3}')
    print(f'total2 : {total2}')
print(f'Total1 : {total1}')

print('.............X Z Y.............')

total1 = 0
for x in range(len(vendas)):
    total2 = 0
    for z in range(len(vendas[0][0])):
        total3 = 0
        for y in range(len(vendas[0])):
            total1 += vendas[x][y][z]
            total2 += vendas[x][y][z]
            total3 += vendas[x][y][z]
        print(f'total3 : {total3}')
    print(f'total2 : {total2}')
print(f'Total1 : {total1}')



