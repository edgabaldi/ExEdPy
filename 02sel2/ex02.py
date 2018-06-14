'''Faça um programa que lê do usuário um caractere e informa se ele é uma vogal, uma consoante
ou não é uma letra.
'''

cat = str(input('Escreva um caracter: ').lower().strip()[0])
if cat.isalpha():
    if cat in 'aeiou':
        print('Você digitou uma vogal')
    else:
        print('Você digitou uma consoante')
else:
    print('Você não digitou uma letra')
