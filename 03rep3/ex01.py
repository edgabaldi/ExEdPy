''' 1º - Projete um algoritmo que leia dois inteiros X e Y e mostrar todos os múltiplos de X
e de Y inferiores a 1000 (inclusive). '''

x = int(input('Digite um valor para X: '))
y = int(input('Digite um valor para Y: '))

print(f'Múltiplos de {x}')
for c in range(0, 1001, x):
    print(c if c !=0 else '', end=' ')

print('')
print(f'Múltiplos de {y}')
for c in range(0, 1001, y):
    print(c if c !=0 else '', end=' ')