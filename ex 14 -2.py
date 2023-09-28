vendas = [

        # Gasolina
        [
           # OR CT OC
            [1, 4, 7, 10],    # Oriente
            [2, 5, 8, 11],    # central
            [3, 6, 9, 12],    # Ocidental
        ],
        # Gasóleo
        [
           # OR CT OC
            [13, 16, 19, 22],  # Oriente
            [14, 17, 20, 23],  # central
            [15, 18, 21, 24],  # Ocidental
        ]

]

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
