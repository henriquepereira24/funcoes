numero = "785554"
resultado = "" # Guarda impares

# %72=1
# 8%2=0
# 5%2=1

for digito in numero:
    if int(digito) % 2 != 0: # 0=Par 1=Impar
        resultado = resultado + digito

print(resultado)
# 1
# 21
# 321
