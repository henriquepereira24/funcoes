produtos = ["Notebook", "Smartphone", "Televisão", "Câmera Digital", "Forno Micro-ondas", "Liquidificador", "Relógio Inteligente", "Fones de Ouvido"]
vendas = [10, 20, 30, 40, 50, 60, 70, 80]

# total das vendas
total = 0

for i in range(0, len(produtos)):
    total += vendas[i]

print(f"Total das Vendas {total}")

# media das vendas
media = total // len(produtos)

print(f"Média das Vendas {media}")

produto_mais_vendido = produtos[0]
quantidade_mais_vendida = vendas[0]

for i in range(0, len(produtos)):
    if vendas[i] > quantidade_mais_vendida:
        quantidade_mais_vendida = vendas[i]
        produto_mais_vendido = produtos[i]

print(f"O produto mais vendido foi {produto_mais_vendido} com {quantidade_mais_vendida} vendas")

quantidade_menos_vendida = vendas[0]
produto_menos_vendido = produtos[0]

for i in range(0, len(produtos)):
    if vendas[i] < quantidade_menos_vendida:
        quantidade_menos_vendida = vendas[i]
        produto_menos_vendido = produtos[i]
print(f"O produto mais vendido foi {produto_menos_vendido} com {quantidade_menos_vendida} vendas")







