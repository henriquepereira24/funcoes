# lista os nomes das ilhas
ilhas = ["Pico", "Faial", "São Jorge", "Terceira", "Graciosa"]
# lista com 5 casas para vendas de cada ilha
vendas = [0, 0, 0, 0, 0]

# varias variaveis para armazenar o total , minimo e maximo
total = minimo = maximo = casa = 0

# loop solicita ao utilizador que insira o valor de vendas para cada ilha, também calcula o total das vendas e atualiza o minimo e o maximo conforme necessário
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
# imprime uma lista das vendas, total de vendas, o valor minimo e o valor maximo.
print(f"vendas: {vendas} total: {total} minimo: {minimo} maximo: {maximo}")

print(f"ilhas com mais vendas [{maximo}]")
for casa in range(len(vendas)):
    if vendas[casa] == maximo:
        print(ilhas[casa])

print(f"ilhas com menos vendas [{minimo}]")
for casa in range(len(vendas)):
    if vendas[casa] == minimo:
        print(ilhas[casa])

media =
for casa in range(len(vendas)):
    if






