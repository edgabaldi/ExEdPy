'''6 – Ler um número N e mostrar todos os múltiplos de 3 inferiores a N. '''


n = int(input('n: '))
for c in range(1, n + 1):
    if c % 3 == 0:
        print(c, end=' ')