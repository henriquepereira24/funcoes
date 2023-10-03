numero = 0

while True:
    digito = int(input("Escreva um dígito (-1 para terminar): "))

    if digito == -1:
        break

    numero = numero * 10 + digito

print("O número é:", numero)
