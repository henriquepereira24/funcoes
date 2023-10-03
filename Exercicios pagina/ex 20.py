
x=1
y = 8
res=''
while x <= 9:
    res = res + str(x)
    print(f'{res}*{x}+{y}={(int(res)*y)+x}')
    x = x + 1