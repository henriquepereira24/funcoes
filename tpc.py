
ilhas = ["Pico", "Faial", "São Jorge", "Terceira", "Graciosa"]
vendas = [0, 0, 0, 0, 0]
totalVendas = 0

# Inserir/Calcular total de vendas
for x in range(len(ilhas)):
    vendas[x] = int(input(f"({ilhas[x]}) Numero de vendas da ilha: "))
    totalVendas = totalVendas + vendas[x]

print(f'\n\nO total de vendas é: {totalVendas}')

# Calcular média das vendas
average = totalVendas // len(ilhas)
print(f"A media de vendas é: {average}")

# Ilhas que venderam mais/menos
Sales = vendas[0]
currentIndex = 0
SalesIndex = 0

for x in vendas:
    if x > Sales:
        Sales = x
        SalesIndex = currentIndex
    currentIndex += 1
print(f"\nIlha com mais vendas é: {ilhas[SalesIndex]}. {Sales} Vendas")

currentIndex = 0
SalesIndex = 0
for x in vendas:
    if x < Sales:
        Sales = x
        SalesIndex = currentIndex
    currentIndex += 1
print(f"Ilha com menos vendas é: {ilhas[SalesIndex]}. {Sales} Vendas")

# Ilhas que venderam mais/menos do que a média
print(f"\nIlhas com vendas superiores à média:")
for x in range(len(ilhas)):
    if vendas[x] > average:
        print(f'{ilhas[x]}')

print(f"Ilhas com vendas inferiores à média:")
for x in range(len(ilhas)):
    if vendas[x] < average:
        print(f'{ilhas[x]}')