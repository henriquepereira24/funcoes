nome = input('Como chamas-te?\n')
numero = int(input('Mete um numero :\n'))



n2 = numero
resultado = 1
while n2 > 0:
    resultado = resultado * n2
    n2 -= 1

print(f'O fatorial do {numero} é : {resultado}')

"""Outro exemplo"""
#def factorial(n):
#    if n == 0:
#        return 1
#    else:
#        return n * factorial(n-1)

#result = factorial(5)
#print(f'Factorial of 5 is:',result)

""""""
