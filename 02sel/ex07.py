'''7 - Dado três valores X, Y, Z, verificar se eles podem ser os comprimentos dos lados de um
triângulo, e se forem, verificar se é um triângulo eqüilátero, isósceles ou escaleno. Se eles
não formarem um triângulo, escrever uma mensagem.
Antes da elaboração do algoritmo, torna-se necessária a revisão de algumas propriedades e
definições:
Propriedade - O comprimento de cada lado de um triângulo é menor do que a soma dos
comprimentos dos outros dois lados.
Definição 1 - Chama-se triângulo eqüilátero aos que tem os comprimentos dos três lados
iguais,
Definição 2 - Chama-se triângulo isósceles ao triângulo que tem os comprimentos de dois
lados iguais.
Definição 3 - Chama-se triângulo escaleno ao triângulo que tem os comprimentos dos três
lados diferentes. '''

from random import randint
print('\nVeja se três retângulos formam algum tipo de triângulo.')

print('\nQuer escolher os números ou deixar o computador escolher?')

opção = str(input('''
[ E ] PARA ESCOLHER
[ P ] PARA O CUNPUTADOR ESCOLHER: ''')).strip().upper()[0]


while opção not in 'EP':
    opção = str(input('''
OPÇÃO INVÁLIDA!!!
[ E ] PARA ESCOLHER
[ P ] PARA O CUNPUTADOR ESCOLHER: ''')).strip().upper()[0]


if opção == 'P':
    v1 = randint(1, 10)
    v2 = randint(8, 10)
    v3 = randint(8, 10)
    if v1 < v2 + v3 and v2 < v3 + v1 and v3 < v1 + v2:
        print(f' Os vetores: {v1} | {v2} | {v3} formam um triângulo',end=' ')
        if v1 == v2 == v3:
            print( 'Equilátero' )
        elif v1 != v2 and v2 != v3 and v3 != v1:
            print( 'Escaleno' )
        else:
            print( 'Isósceles' )
    else:
        print(f' Os vetores: {v1} | {v2} | {v3} não formam um triângulo')
else:
    v1 = int(input('1º vetor: '))
    v2 = int(input('2º vetor: '))
    v3 = int(input('3º vetor: '))
    if v1 < v2 + v3 and v2 < v3 + v1 and v3 < v1 + v2:
        print(f' Os vetores: {v1} | {v2} | {v3} formam um triângulo', end=' ')
        if v1 == v2 == v3:
            print('Equilátero')
        elif v1 != v2 and v2 != v3 and v3 != v1:
            print('Escaleno')
        else:
            print('Isósceles')
    else:
        print(f' Os vetores: {v1} | {v2} | {v3} não formam um triângulo')



