# Calcular Salário
# Pergunta nome, horas, Preço Hora, Vendeu
# seg.social = 11%
# horas 0 - 40 Preço Normal
#       41 - 60 Preço 1.5 x
#       61 - ... Preço 2.0 x
# Vendas: 10000 - 1%, 20000 - 2%, 30000 - 3%, 40000 - 4%, ... %5

seguranca_social = 0.11
vendaextra = 0
salario = 0

nome = input('Como te chamas?')
horas = float(input('Quantas horas trabalhas?'))
ganho = float(input('Quanto ganhas por hora?'))
venda = float(input('Quanto que tu vendeste?'))

if 0 < venda <= 10000:
    vendaextra = venda * 0.01
elif 10001 < venda <= 20000:
    vendaextra = venda - 10000
    vendaextra *= 0.02
    vendaextra += 100
elif 20000 < venda <= 30000:
    vendaextra = venda - 20000
    vendaextra *= 0.03
    vendaextra += 300
elif 30000 < venda <= 40000:
    vendaextra = venda - 30000
    vendaextra *= 0.04
    vendaextra += 600
elif venda >= 40000:
    vendaextra = venda - 40000
    vendaextra *= 0.05
    vendaextra += 1000

if horas <= 40:
    salario = horas * ganho
if 41 <= horas <= 60:
    salario = 40 * ganho + (horas - 40) * ganho * 1.5
if horas >= 61:
    salario = 40 * ganho + 20 * ganho * 1.5 + (horas - 60) * ganho * 2

salario += vendaextra
desconto = salario * seguranca_social
salario -= desconto

print(
    f'Nome: {nome}\nTrabalhas: {horas} horas\nGanhas: {ganho}€ por hora\nVendeste: {venda}\n\nRecebeste o bonus de vendas de: {vendaextra}€\nSalario final: {salario}€')