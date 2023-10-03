""" #ex11
Escreva um programa em Python que lê um número inteiro positivo e
produz o número correspondente a inverter a ordem dos seus dígitos.

Por exemplo
Escreva um inteiro positivo
? 7633256
O número invertido é 6523367
"""

numerointeiro = input("Escreva um numero inteiro positivo: ") #12345
invertido = ""

# if "-" in numerointeiro:
#     invertido = "INSERE UM NUMERO POSITIVO"
# else:

for digito in numerointeiro:
    invertido = digito + invertido # digito tem que vir primeiro  

print(f'O numero invertido é: {invertido}')

#123

# 54321

# 1
# 21
# 321