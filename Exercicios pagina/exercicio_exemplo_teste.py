soma = 1

print("Qual o valor de x")
x = int(input("? "))                # meto 5
soma += x                           

print("Qual o valor de n")
n = int(input("? "))                # meto 3

ultimoTermo = x
for pos in range(2, n + 1):        # 2-5
    ultimoTermo = ultimoTermo * x / pos
    soma += ultimoTermo

print("O valor da soma é ", soma) #39.3