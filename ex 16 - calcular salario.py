# Calcular Salário
# Pergunta nome, horas, Preço Hora, Vendeu
# seg.social = 11%
# horas 0 - 40 Preço Normal
#       41 - 60 Preço 1.5 x
#       61 - ... Preço 2.0 x
# Vendas: 10000 - 1%, 20000 - 2%, 30000 - 3%, 40000 - 4%, ... %5

nome = input('Como se chama:')
horas = int(input('Quantas horas trabalhou:'))
preco_hora= float(input('Quanto ganhas à hora:'))
vendas = int(input('Quanto vendeu:'))


#nome = input('Como te chamas?'))
#horas = int(input('quantas horas trabalhadas?'))
#vendas = float(input('quantas vendas?'))
#por_hora = float(input('preco por hora?'))





segurancaSocial = 0.11
percentagem_de_vendas = 0.0
desconto = 0.0
salarioLiquido = 0
salarioBruto = 0.0



#desconto

resto = 0
resto_de_vendas = vendas

i = 0.01
if vendas >= 10000:
    resto = 10000 * i
    i += 0.01
    resto_de_vendas = resto_de_vendas - 10000
if vendas >= 20000:
    resto += (10000 * i)
    i += 0.01
    resto_de_vendas = resto_de_vendas - 10000
if vendas >= 30000:
    resto += (10000 * i)
    i += 0.01
    resto_de_vendas = resto_de_vendas - 10000
if vendas >= 40000:
    resto += (10000 * i)
    i += 0.01
    resto_de_vendas = resto_de_vendas - 10000
if resto != 0:
    resto += (resto_de_vendas * i)
    i += 0.01
print(resto_de_vendas)
print(resto)


#preco por hora
if horas  <= 40:
    print('horas trabalhadas: 0 - 40 preco normal')
    salarioBruto = horas * preco_hora
    salarioBruto = salarioBruto + (vendas * percentagem_de_vendas)
    desconto = salarioBruto * segurancaSocial
    salarioLiquido = salarioBruto - desconto
elif horas <= 60:
    print('horas trabalhadas: 41 - 60 1.5x')
    salarioBruto = 40 * preco_hora
    resto_das_horas = horas - 40
    salarioBruto = salarioBruto + resto_das_horas * preco_hora * 1.5
    desconto = salarioBruto * segurancaSocial

else:
    print('horas trabalhadas: 61 < preco 2.0x')

salarioBruto = salarioBruto + resto

print(f'salarioBruto-{salarioBruto}')
print(f'desconto-{desconto}')
print(f'salarioLiquido-{salarioLiquido}')