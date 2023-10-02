#Inserir um texto
#quantas vezes apareçe cada letra?
#apresenta do maior para o menor


texto = input('Escreve um texto:\n')
texto = texto.lower()
contagem = {}


for letra in texto:
    if letra in contagem:
        contagem[letra] += 1
    else:
        contagem[letra] = 1

print(contagem)

letras = []
valores = []
