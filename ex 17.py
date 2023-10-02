# [] -> lista () -> tuplo {} -> dicionário {} -> conjunto
vendas = {}
vendas['Terceira'] = 1
vendas['Pico'] = 2
vendas['São Jorge'] = 3

print(vendas)

ilhas = ['São Jorge', 'Faial', 'Graciosa']

for ilha in ilhas:
    vendas[ilha] = int(input(f'Vendas para {ilha}?'))

print(vendas)

for ilha in vendas:
    vendas[ilha] = vendas[ilha] * 2

print(vendas)

for k in vendas.values():
    print(k) # aceder aos valores

for v in vendas.keys():
    print(v) # aceder as keys

for z in vendas.pop('Faial'):
    print(z)




