
num = int(input('Inserir Numero:\n'))
n = []


for x in str(num):
    n.append(x)

zeros = 0
for idx in range(len(n) - 1):
    if n[idx] == 0:
        if n[idx+1] == 0:
            zeros += 1
print (f'O Zero aparece {zeros}')