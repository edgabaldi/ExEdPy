'''Faça um programa que requisita do usuário 3 (três) números inteiros para apostar num bingo e depois requisita os 3 (três) inteiros que foram sorteados. Finalmente, o programa deve informar quantos números o usuário acertou no sorteio (0, 1, 2 ou 3 acertos).'''


from random import randint

jogador = [randint(0, 9), randint(0, 9), randint(0, 9)]
bingo = [randint(0, 9), randint(0, 9), randint(0, 9)]
print(f'jogador {jogador}')

print(f'  bingo {bingo}')

s = 0
for c in range(0, 3):
    if jogador[c] in bingo:
        s +=1
print(f'{s} Acerto(s)')