''' 6º - Em Matemática, um número perfeito é um número inteiro para o qual a soma de
todos os seus divisores positivos próprios (excluindo ele mesmo) é igual ao próprio
número. Por exemplo, o número 6 é um número perfeito, pois: 6 = 1 + 2 + 3
O próximo número perfeito é o 28, pois: 28 = 1 + 2 + 4 + 7 + 14
Projete um algoritmo que leia um número N e informe se ele é um número perfeito. '''

n = int(input('n: '))
lnd = []
s = 0
for c in range(1, n):
    if n % c == 0:
        lnd.append(c)
        s += c
if s == n:
    print('Número é perfeito')
else:
    print('Número não é perfeito')