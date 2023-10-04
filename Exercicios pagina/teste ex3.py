pessoas = []
pessoa = {}
while True:
    pessoa['nome'] = input('Nome: ')
    pessoa['idade'] = int(input('Idade: '))
    pessoa['telefone'] = input('Telefone: ')
    pessoas.append(pessoa.copy())
    if input('Deseja inserir mais uma pessoa? ') not in ('s', 'sim'):
        break

print('--- Usando for ---')
for p in pessoas:
    print(f'Nome: {p["nome"]}, Idade: {p["idade"]}, Telefone: {p["telefone"]}')
print('--- Usando for com range ---')
for p in range(pessoas):
print('--- Usando while ---')
y=0
while y < len(pessoas):
    print(f'Nome: {pessoas[y]["nome"]}, Idade: {pessoas[y]["idade"]}, Telefone: {pessoas[y]["telefone"]}')
    y += 1
