# VENDAS DE COMBUSTIVEL
# TOTAL
# TOTAL POR ESTAÇÃO
# TOTAL POR GRUPO
# Qual estação que tem mais vendas
# Qual o grupo que vendeu menos
# Pode haver mais que uma, o mesmo com os grupos

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
estacao = ['Verão','Outono','Inverno','Primavera']
grupos = ['Oriental','Central','Ocidental']



total1 = 0
for x in range(len(vendas)):
    total2 = 0
    for y in range(len(vendas[0])):
        total3 = 0
        for z in range(len(vendas[0][0])):
            total1 += vendas[x][y][z]
            total2 += vendas[x][y][z]
            total3 += vendas[x][y][z]
print(f'Total de vendas de combustivel : {total1}')



print('.............Y X Z.............')

total1 = 0
for y in range(len(vendas[0])): # Muda de lista Gasolina ou gasoleo
    total2 = 0
    for x in range(len(vendas)): # Casas de cada lista
        total3 = 0
        for z in range(len(vendas[0][0])): # Corre as listas na vertical
            total1 += vendas[x][y][z]
            total2 += vendas[x][y][z]
            total3 += vendas[x][y][z]

    print(f'O total para {estacao[y]} é {total2}')
print(f'A estação que vendeu mais foi {estacao[y]}')


print('.............Z Y X.............')
total1 = 0
for z in range(len(vendas[0][0])): # Muda de lista Gasolina ou gasoleo
    total2 = 0
    for y in range(len(vendas[0])): # Casas de cada lista
        total3 = 0
        for x in range(len(vendas)): # Corre as listas na vertical
            total1 += vendas[x][y][z]
            total2 += vendas[x][y][z]
            total3 += vendas[x][y][z]
    print(f'O total para {grupos[z]} é {total2}')
print(f'O grupo que vendeu menos foi {grupos[z]}')



