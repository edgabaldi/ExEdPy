'''Um aluno de computação está organizando um bolão de futebol. Segundo suas regras, os apostadores informam o placar do jogo e

ganham 10 pontos se acertarem o vencedor ou se foi empate

ganham mais 5 pontos para o placar de cada time que acertarem

Exemplo: se o placar do jogo foi 3x2, são 0 pontos se o placar apostado foi 0x1; 5 pontos para os placares apostados 0x2 ou 3x5; 10 pontos para o placar apostado 1x0; ou 20 pontos para o placar exato de 3x2. Faça um programa que requisita do usuário o placar apostado e depois o placar do jogo e
informa quantos pontos o apostador fez.'''
from random import randint

print('\nAcerte o Placar e ganhe pontos: \n')

ta = int(input('Time A, Gol(s): '))
tb = int(input('Time B, Gol(s): '))

pta = randint(0, 2)
ptb = randint(0, 2)
print('='*25)
print(f'{"PLACAR DO JOGO":^25}')
print(f'[Time A]  {pta} x {ptb}  [Time B]')


p = 0
if pta > ptb:
    print(f'{"Vitória do [Time A]":^25}')
elif pta < ptb:
    print(f'{"Vitória do [Time B]":^25}')
else:
    print(f'{"Empate":^25}')
print('='*25)

if ta > tb and pta > ptb or ta < tb and pta < ptb or ta == tb == pta == ptb:
    p += 10
    print('Acertou o Resultado\n(Vencedor ou Empate)\nGanhou 10 pontos')
if ta == pta:
    p += 5
    print('Acertou placar do [Time A]\nGahou 5 pontos')
if tb == ptb:
    p += 5
    print('Acertou placar do [Time B]\nGahou 5 pontos')
if p == 0:
    print('Você não acertou nada!!!')
print(f'Total de ponto: {p}')