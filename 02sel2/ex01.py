'''1. Crie um programa que lê três inteiros e informa VERDADEIRO se apenas o maior deles é par
ou se o menor deles é ímpar ou informa FALSO em caso contrário.'''
n1 = int(input('nº: '))
n2 = int(input('nº: '))
n3 = int(input('nº: '))
maior = menor = 0
i = 1
while i == 1:
    menor = n1
    maior = n1
    i += 1

if n3 < n2 > n1:
    maior = n2
if n2 < n3 > n1:
    maior = n3
if n3 > n2 < n1:
    menor = n2
if n2 > n3 < n1:
    menor = n3
if maior % 2 == 0 or menor % 2 != 0:
    print('Verdadeiro')
else:
    print('Falso')

    