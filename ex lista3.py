produtos = ["Macbook Air", "Macbook Pro", "iPhone "]
vendas = [10, 15, 25]

soma = 0

for i in range(len(produtos)):
    soma += vendas[i]

print(f"Soma das Vendas {soma}")

media= soma // len(produtos)

print(f"Média das Vendas {media}")

produto_mais_vendido = produtos[0]
quantidade_mais_vendido = vendas[0]

for i in range(len(produtos)):
    if vendas[i] > quantidade_mais_vendido:
        produto_mais_vendido = produtos[i]
        quantidade_mais_vendido = vendas[i]

print(f"produtos mais vendidos: {quantidade_mais_vendido} com {produto_mais_vendido}")

quantida_menos_vendidos = vendas[0]
produto_menos_vendidos = produtos[0]

for i in range(len(produtos)):
    if vendas[i] < quantida_menos_vendidos:
        produto_menos_vendidos = produtos[i]
        quantida_menos_vendidos = vendas[i]

print(f"produtos menos vendidos: {quantida_menos_vendidos} com {produto_menos_vendidos}")



