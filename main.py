## Função Calculadora ##

def aritemetica(op,n1,n2):
    if op == '+':
        resultado = n1 + n2
    elif op == '-':
        resultado = n1 - n2
    elif op == '*':
        resultado = n1 * n2
    elif op == '/':
        resultado = n1 / n2
    else:
        resultado = 'Operação Inválida'
    return resultado


def contas(op, n1, n2):
    if op == '+':
        resultado = n1 + n2
    else:
        if op == '-':
            resultado = n1 - n2
        else:
            if op == '*':
                resultado = n1 * n2
            else:
                if op == '/':
                    resultado = n1 / n2
                else:
                    resultado = 'Opereção Invalida'
    return resultado


def continhas(op, n1, n2):
    resultado = 'Operação Inválida'
    if op == '+':
        resultado = n1 + n2
    if op == '-':
        resultado = n1 - n2
    if op == '*':
        resultado = n1 * n2
    if op == '/':
        resultado = n1 / n2

    return resultado

print(aritemetica('+', 2, 4))
print(aritemetica('-', 2, 4))
print(aritemetica('*', 2, 4))
print(aritemetica('/', 2, 4))
print(aritemetica('bla', 2, 4))
print('____________')
print(contas('+', 2, 4))
print(contas('-', 2, 4))
print(contas('*', 2, 4))
print(contas('/', 2, 4))
print(contas('bla', 2, 4))
print('____________')
print(continhas('+', 2, 4))
print(continhas('-', 2, 4))
print(continhas('*', 2, 4))
print(continhas('/', 2, 4))
print(continhas('bla', 2, 4))
