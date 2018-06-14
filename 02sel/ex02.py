'''2 – Faça um algoritmo que leia os valores A, B, C e diga se a soma de A + B é menor que C. '''
A = int(input('Valor para A: '))
B = int(input('Valor para B: '))
C = int(input('Valor para C: '))

if A + B < C:
    print(f'A soma entre {A} e {B} é menor que {C}')
else:
    print(f'A soma entre {A} E {B} NÃO é menor que {C}')