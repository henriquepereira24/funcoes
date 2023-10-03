#Escreva um programa que lê um inteiro e calcula a soma dos seus dígitos.

numero = str(input('Escreve um número:'))

soma = 0

for x in numero:
    soma += int(x)


print(f'A Soma dos dois valores é:\n{soma}')