'''4. Escreva um programa que lê do usuário 4 (quatro) números inteiros e informa se há ou não um deles no           intervalo entre 1 e 25
        outro de 26 a 50,
        outro de 51 a 75
  e um último de 76 a 100.'''

from random import randint
c1 = c2 = c3 = c4 = 0
sorteados = []
print('\nNúmeros sorteados: ',end='')
for i in range(1, 5):
    n = randint(1, 100)
    sorteados.append(n)
    if n in range(1, 26):
        c1 += 1
    if n in range(26, 51):
        c2 += 1
    if n in range(51, 76):
        c3 += 1
    if n in range(76, 101):
        c4 += 1
print(sorted(sorteados))
if c1 > 0:
    print(f'\nHá {c1} elemento(s) entre 1 e 25')
if c2 > 0:
    print(f'\nHá {c2} elemento(s) entre 26 e 50')
if c3 > 0:
    print(f'\nHá {c3} elemento(s) entre 51 e 75')
if c4 > 0:
    print(f'\nHá {c4} elemento(s) entre 76 e 100')