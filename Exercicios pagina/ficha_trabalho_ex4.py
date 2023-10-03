"""
Escreva um programa que lê um número inteiro correspondente a um
certo número de segundos e que escreve o número de dias, horas, minutos
e segundos correspondentes a esse número. Por exemplo,

Escreva o número de segundos 345678
dias: 4 horas: 0 mins: 1 segs: 18
"""
numero = int(input(345678))
dias = horas = minutos = segundos = 0

while numero != 0:
    if numero >= 86400: # 1 dia em segundos
        numero -= 86400
        dias += 1
    elif numero >= 3600: # 1 hora em segundos
        numero -= 3600
        horas += 1
    elif numero >= 60: # 1 minuto
        numero -= 60
        minutos += 1
    elif numero > 0:
        numero -= 1
        segundos += 1

print(f"Dias: {dias}")
print(f"Horas: {horas}")
print(f"Minutos: {minutos}")
print(f"Segundos: {segundos}")


