# escrever segundos para fazer a conversão para dias

segundos = 0

while segundos >= 0:
    segundos = int(input('Escreve os segundos:\n'))
    dias = segundos / 86400 # 60*60*60*24 (s/m/h/d)
    if segundos >= 0:
        print(dias)