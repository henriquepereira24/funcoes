quantia = float(input("Digite a quantia em Euros: "))

ciquenta = vinte = dez = cinco = dois = um = 0.0
fiftycent = twentycent = tencent = fivecent = twocent = onecent = 0.0

while quantia != 0:
    if quantia >= 50:
        quantia = quantia - 50
        ciquenta += 1
    elif quantia >= 20:
        quantia = quantia - 20
        vinte += 1
    elif quantia >= 10:
        quantia = quantia - 10
        dez += 1
    elif quantia >= 5:
        quantia = quantia - 5
        cinco += 1
    elif quantia >= 2:
        quantia = quantia - 2
        dois += 1
    elif quantia >= 1:
        quantia = quantia - 1
        um += 1
    elif quantia >= 0.50:
        quantia = round(quantia - 0.50, 2)
        fiftycent += 1
    elif quantia >= 0.20:
        quantia = round(quantia - 0.20, 2)
        twentycent += 1
    elif quantia >= 0.10:
        quantia = round(quantia - 0.10, 2)
        tencent += 1
    elif quantia >= 0.05:
        quantia = round(quantia - 0.05, 2)
        fivecent += 1
    elif quantia >= 0.02:
        quantia = round(quantia - 0.02, 2)
        twocent += 1
    elif quantia >= 0.01:
        quantia = round(quantia - 0.01, 2)
        onecent += 1

print(f'notas: 50,{ciquenta}, 20,{vinte}, 10,{dez}, 5,{cinco}, 2,{dois}, 1,{um}')
print(f'moedas: 50({fiftycent}) 20({twentycent}) 10({tencent}) 5({fivecent}) 2({twocent})  1({onecent})')
