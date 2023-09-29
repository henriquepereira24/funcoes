#cria lista com nomes das ilhas
#pede valores para cada ilha
#apresenta :total de ilhas, valor minimo e ilhas com esse valor, valor maximo e ilhas com esses valor
#ordena de crescente e decrescente

ilhas = ["Pico", "Faial", "São Jorge", "Terceira", "Graciosa"]
ilhasmenor = []
ilhasmaior = []
vendas = [0, 0, 0, 0, 0]

total = minimo = maximo = casa = 0

for i in range(len(ilhas)):
    vendas[casa] = (int(input(f"Digite o valor de {ilhas[i]}: ")))
    total += vendas[casa]
    if casa == 0:
        minimo = vendas[casa]
        maximo = vendas[casa]
    else:
        if vendas[casa] < minimo:
            minimo = vendas[casa]
        if vendas [casa] > maximo:
            maximo = vendas[casa]
    casa += 1

print(f"vendas: {vendas} total: {total} minimo: {minimo} maximo: {maximo}")

for casa in range(len(vendas)):
    if vendas[casa] == minimo:
        ilhasmenor.append(ilhas[casa])
    if vendas[casa] == maximo:
        ilhasmaior.append(ilhas[casa])

print(f"ilhas com menor venda: {ilhasmenor} Menor valor: {minimo}")
print(f"ilhas com maior venda: {ilhasmaior} Maior valor: {maximo}")

