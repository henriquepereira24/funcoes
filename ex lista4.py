# lista do alunos
alunos = ["Maria", "João", "Pedro","Isabel"]
# lista de notas
notas = [8.5, 7.5, 6.5, 5]
# média dos alunos
media = sum(notas) / len(notas)
# print media
print(f"A média das notas é de {media}")
# duas variáveis, aluno_maior_nota e notas_maior_nota, com os valores do primeiro aluno (Maria) e sua nota correspondente (8.5).
aluno_maior_nota= alunos[0]
notas_maior_nota = notas[0]
# for para procurar os alunos com maior nota
for i in range(len(alunos)):
    if notas[i] > notas_maior_nota:
        aluno_maior_nota = alunos[i]
        notas_maior_nota = notas[i]

print(f"O melhor aluno foi {aluno_maior_nota} e a nota foi de {notas_maior_nota}")
#duas variáveis, aluno_menor_nota e notas_menor_
aluno_menor_nota = alunos[0]
notas_menor_nota = notas[0]
# for para procurar os alunos com menor nota
for i in range(len(alunos)):
    if notas[i] < notas_menor_nota:
        aluno_menor_nota = alunos[i]
        notas_menor_nota = notas[i]

print(f"O pior aluno foi {aluno_menor_nota} e a nota foi de {notas_menor_nota}")

for i in range(len(alunos)):
    if notas[i] > media:
        print(f"O aluno {alunos[i]} foi aprovado com {notas[i]}")
    if notas[i] < media:
        print(f"O aluno {alunos[i]} foi reprovado com {notas[i]}")


