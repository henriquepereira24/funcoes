produtos = ["Produto1", "Produto2", "Produto3", "Produto4", "Produto5"]
vendas = [0, 0, 0, 0, 0]

total = mais_vendas = menos_vendas = casa = 0

for i in range(len(produtos)):
    vendas[casa] = (int(input(f'Quantidade de {produtos[i]}:')))
    total += vendas[casa]
    if casa == 0:
        mais_vendas = vendas[casa]
        menos_vendas = vendas[casa]
    else:
        if vendas[casa] > mais_vendas:
            mais_vendas = vendas[casa]
        if vendas[casa] < menos_vendas:
            menos_vendas = vendas[casa]
    casa += 1


print(f'Total de vendas: {total}, Maximo de vendas: {mais_vendas}, Menor de vendas: {menos_vendas}')

for casa in range(len(produtos)):
    if vendas[casa] == mais_vendas:
        print(f'Produto mais vendido: {produtos[casa]}')

    if vendas[casa] == menos_vendas:
        print(f'Produto menos vendido: {produtos[casa]}')