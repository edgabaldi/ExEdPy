'''5 - Mostrar todos os múltiplos de 5 inferiores a 1000. '''

for c in range(1, 1001):
    if c % 5 == 0:
        print(c, end=' ')

''' ou '''

for c in range(0, 1001, 5):
    print(c if c != 0 else '', end=' ')
