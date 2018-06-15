'''3 – Ler um número N, somar todos os números inteiros entre 1 e N, e mostre o resultado
obtido. '''

n = int(input('N: '))
s = 0
for c in range(1, (n + 1)):
    print(c, end='')
    print(' + ' if c < n else ' = ', end='')
    s += c
print(s)