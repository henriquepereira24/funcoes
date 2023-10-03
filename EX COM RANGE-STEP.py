for x in range (1, 24, 3):
    print(x)

    numeros = int(input("Quantos números deseja somar? "))

    soma = 0

    for x in range(numeros):
        numero = int(input(f"Digite o {x + 1} número: "))
        soma += numero

    print(f"A soma dos números é: {soma}")