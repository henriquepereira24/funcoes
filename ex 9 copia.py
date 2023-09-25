ilhas = ["Pico", "Faial", "São Jorge", "Terceira", "Graciosa"]
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
        if vendas[casa] > maximo:
            maximo = vendas[casa]
    casa += 1

print(f"vendas: {vendas} total: {total} minimo: {minimo} maximo: {maximo}")

print(f"ilhas com mais vendas [{maximo}]")
for casa in range(len(vendas)):
    if vendas[casa] == maximo:
        print(ilhas[casa])

print(f"ilhas com menos vendas [{minimo}]")
for casa in range(len(vendas)):
    if vendas[casa] == minimo:
        print(ilhas[casa])



if vendas[x] > vendas[x+1]:
    suporte = vendas[x]
    vendas[x] = vendas[x+1]
    vendas[x+1] = suporte
    troquei = True




