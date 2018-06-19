'''5º - Projete um algoritmo para ler uma lista de inteiros terminada pelo número 101.
Cada inteiro representa a nota de um aluno em uma disciplina (variando de 0 a 100).
Ao final o algoritmo deve mostrar quantos alunos tiveram nota maior ou igual a 70. '''

s = 0
while True:
    n = int(input('Nota de 0 a 100: '))
    if n == 101:
        break
    else:
        if 0 <= n <=100:
            if n >= 70:
                s += 1
        else:
            print('Opção inválda!')
print(f'{s} alunos tiveram notas acima maior ou igual a 70')

