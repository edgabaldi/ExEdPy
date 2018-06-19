'''7º - Ler um inteiro N e verificar se ele é um número primo'''
p = np = 0
n = int(input('n: '))
for c in range(1, n+1):
    if n % c == 0:
       p += 1
       print(f'\033[33m{c}\033[m', end=' ')
    else:
        print(f'\033[31m{c}\033[m', end=' ')
        np += 1
print('')
if p > 2:
    print(f'{n} não é primo')
else:
    print(f'{n} é primo')
