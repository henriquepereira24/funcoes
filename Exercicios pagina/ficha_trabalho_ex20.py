y = 8
res = ""

for x in range(1, 10):
    res += str(x)
    print(f'{res} * {y} + {x} = {int(res) * y + x}')
    