# Apresenta vendas de combustivel
# - Total
# - Total por estação
# - Total por grupo
# Qual a estação que tem mais vendas
# Qual o grupo que tem menos vendos
# - Pode haver mais que uma, o mesmo com os grupos

vendas = [
    # Gasolina
    [
        # OR CT OC
        [1, 2, 3],  # Verão
        [4, 5, 6],  # Outono
        [7, 8, 9],  # Inverno
        [10, 11, 12]  # Primavera
    ],
    # Gasóleo
    [
        [13, 14, 15],  # Verão
        [16, 17, 18],  # Outono
        [19, 20, 21],  # Inverno
        [22, 23, 24]  # Primavera
    ]
]

estacoes = ["Verão", "Outono", "Inverno", "Primavera"]
grupos = ["Oriental", "Central", "Ocidental"]

valoresGrupos = []
valoresEstacoes = []

total1 = 0
for y in range(len(vendas[0])): # Lista
    total2 = 0
    for x in range(len(vendas)): # Gasolina/Gasoleo
        total3 = 0
        for z in range(len(vendas[0][0])): # Casa
            total1 += vendas[x][y][z]
            total2 += vendas[x][y][z]
            total3 += vendas[x][y][z]
    print(f'{estacoes[y]} | Total = {total2}')
    valoresEstacoes.append(total2)

print()

total1 = 0
for z in range(len(vendas[0][0])):
    total2 = 0
    for y in range(len(vendas[0])):
        total3 = 0
        for x in range(len(vendas)):
            total1 += vendas[x][y][z]
            total2 += vendas[x][y][z]
            total3 += vendas[x][y][z]
    print(f'Total do grupo {grupos[z]} = {total2}')
    valoresGrupos.append(total2)

print()

maior = 0
currentIndex = 0
maxIndex = 0

# Estações maiores
for x in range(len(valoresEstacoes)):
    if valoresEstacoes[x] > maior:
        maior = valoresEstacoes[x]
        maxIndex = x
    currentIndex += 1

print(f'A estação com maior venda é de {maior} estações:')
for x in range(len(valoresEstacoes)):
    if valoresEstacoes[x] == maior:
        print(estacoes[x])

# Estações menores
currentIndex = 0
maxIndex = 0
for x in range(len(valoresGrupos)):
    if valoresGrupos[x] < maior:
        maior = valoresGrupos[x]
        maxIndex = x
    currentIndex += 1

print(f'O grupo com menor venda é de {maior} na(s) ilha(s):')
for x in range(len(valoresGrupos)):
    if valoresGrupos[x] == maior:
        print(grupos[x])

print(f'\nTotal Final: {total1}')
