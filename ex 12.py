def calcular(valor1, valor2, op='+'):

    total = 'Código de operação inválido'
    if op == '+':
        total = valor1 + valor2
    if op == '-':
        total = valor1 - valor2
    if op == ':':
        total = valor1 / valor2
    if op == '*':
        total = valor1 * valor2

    return total

def vendas(valor1, valor2):

    total= 0

    for i in range(len(produtos)):
        total += vendas[i]

    print(total)




if __name__ == '__main__':
    produtos = ['Telemovel', 'PC', 'Teclado', 'Ecrã']
    vendas = [12, 23, 27, 19]
    print(vendas())
    valor1 = int(input('Digite o primeiro valor: '))
    valor2 = int(input('Digite o segundo valor: '))
    operador = input('Digite o operador (+, -, /, *): ')
    print(calcular(valor1, valor2, operador))

