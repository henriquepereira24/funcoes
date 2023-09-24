alunos = ["Maria", "João", "Pedro","Isabel"]
notas = [8.5, 7.5, 6.5, 5]

media = sum(notas) / len(notas)

print(f"A média das notas é de {media}")

aluno_maior_nota= alunos[0]
notas_maior_nota = notas[0]

for i in range(len(alunos)):
    if notas[i] > notas_maior_nota:
        aluno_maior_nota = alunos[i]
        notas_maior_nota = notas[i]

print(f"O melhor aluno foi {aluno_maior_nota} e a nota foi de {notas_maior_nota}")

aluno_menor_nota = alunos[0]
notas_menor_nota = notas[0]

for i in range(len(alunos)):
    if notas[i] < notas_menor_nota:
        aluno_menor_nota = alunos[i]
        notas_menor_nota = notas[i]

print(f"O pior aluno foi {aluno_menor_nota} e a nota foi de {notas_menor_nota}")

for i in range(len(alunos)):
    if notas[i] > media:
        print(f"O aluno {alunos[i]} foi aprovado com {notas[i]}")


