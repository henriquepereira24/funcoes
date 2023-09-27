vendas = [
    [1,
]

tipos = ['Gasolina', 'Gasóleo']
grupo_ilhas = ['Oriental', 'Central', 'Ocidental']
estacoes = ["Verão","Outono","Inverno","Primavera"]

total = 0
for x in range(len(vendas)):
    totaltipo = 0
    for y in range(len(vendas[x])):
        totaltipo += vendas[x][y]
    print(f'Total de vendas de {tipos} = {totaltipo}')
    total += totaltipo
print(f'Total de Vendas = {total}')

