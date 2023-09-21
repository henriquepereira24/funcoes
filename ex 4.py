"""
Quantidade numeros numa lista entre 0 e 10, 11 - 20, 21 - 30, 31 - 40, 41 - 50 depois de 50 para cima
"""

list = [10, 8, 80, 49, 20, 41, 20, 25, 34, 27]

range_0_10 = 0
range_11_20 = 0
range_21_30 = 0
range_31_40 = 0
range_41_50 = 0

for number in list:
    if 0 <= number <= 10:
        range_0_10 += 1
    elif 11 <= number <= 20:
        range_11_20 += 1
    elif 21 <= number <= 30:
        range_21_30 += 1
    elif 31 <= number <= 40:
        range_31_40 += 1
    elif 41 <= number <= 50:
        range_41_50 += 1

print("Number of numbers between 0 and 10:", range_0_10)
print("Number of numbers between 11 and 20:", range_11_20)
print("Number of numbers between 21 and 30:", range_21_30)
print("Number of numbers between 31 and 40:", range_31_40)
print("Number of numbers between 41 and 50:", range_41_50)