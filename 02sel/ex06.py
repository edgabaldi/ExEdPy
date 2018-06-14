'''6 - Faça um algoritmo que leia o nome e as três notas de uma disciplina de um aluno e ao
final escreva o nome do aluno, sua média e se ele foi aprovado. A média mínima para
aprovação é 8.'''

al = str(input('Nome do aluno: '))
s = 0
for n in range(1,4):
    n = float(input(f'{n}ª nota: '))
    s += n
media = s / 3
if media >= 8:
    print(f'{al} ficou com média {media:.1f} e está aprovado!')
else:
    print(f'O Aluno {al} ficou com média {media:.1f} e foi reprovado!')
