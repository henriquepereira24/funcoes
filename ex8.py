
# Criar uma lista com os nomes do grupo central.
# Criar uma lista com 5 casas, inicializadas a zero.
# Pede ao utilizador para inserir vendas para cada ilha.


ilhas = ['Terceira', 'Graciosa', 'São Jorge', 'Faial', 'Pico']
vendas = [0, 0, 0, 0, 0]
#         0  1  2  3  4

y=0
verificar=0

for x in range(len(vendas)):
    while  y < 5:
        vendas[y] = int(input(f' Insere as vendas para {ilhas[y]}:'))
        verificar += vendas[y]
        y += 1
print(f'Total de vendas:{verificar}')


#TPC
# ilhas e montantes que venderam mais
# ilhas e montantes que venderam menos
# ilhas e montantes que venderam mais que a média
# ilhas e montantes que venderam mmenos que a média