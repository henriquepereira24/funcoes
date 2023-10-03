
horas = int(input(f'Quantas horas semanais fizeste?\n'))
salario_hora = int(input(f'Quantas recebes á hora?\n'))


if horas <= 40:
    salario = salario_hora * horas
elif horas > 40:
    salario_extra = (salario_hora * 2) * (horas - 40)
    salario =  salario_extra + (salario_hora * 40)

print(f'Salário total: {salario}')




