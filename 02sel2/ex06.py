'''Elabore um programa que recebe do usuário três cadeias de caracteres e informa
VERDADEIRO se há pelo menos duas diferentes cadeias iguais aos valores 'azul', 'preto'ou
'vermelho' ou FALSO em caso contrário. Exemplos: {'azul', 'preto', 'branco'} é VERDADEIRO;
{'azul', 'roxo', 'azul'} é FALSO; {'preto', vermelho', 'vermelho'} é VERDADEIRO.'''
from random import randint

cores = ['azul', 'preto', 'vermelho', 'branco', 'amarelo']
lista = []

for i in range(1, 4):
    lista.append(cores[randint(0, 4)])
print(lista)

a1 = lista.count('vermelho')
a2 = lista.count('azul')
a3 = lista.count('preto')

if a1 == 2 or a2 == 2 or a3 == 2:
    print('VERDADEIRO')
else:
    print('FALSO')