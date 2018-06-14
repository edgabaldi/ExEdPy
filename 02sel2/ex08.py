'''Em uma competição de saltos ornamentais, 6 (seis) juízes informam notas reais variando de 0 a 10. A nota final do atleta deve excluir a maior e a menor nota dos juízes e é composta pela soma das quatro demais notas. Faça um programa que lê do usuário as seis notas dos juízes e informa
a nota final do atleta (a soma das notas excluindo a menor e a maior delas).'''

from random import randint
notas = []
soma_notas = 0
for nota in range(1, 7):
    nota_juiz = randint(1, 10)
    notas.append(nota_juiz)
    soma_notas += nota_juiz

maior_nota = max(notas)
menor_nota = min(notas)
nota_final = soma_notas - maior_nota - menor_nota

print('Notas:')
print(f'{notas}')
print('Notas descartadas:')
print(f'Maior nota: {maior_nota}')
print(f'Menor nota: {menor_nota}')
print(f'Nota final do Atleta: {nota_final} ')