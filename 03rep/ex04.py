'''4 – Ler uma lista de números terminada pelo numero 999 e mostre cada numero lido. Ao
final o programa deve mostrar o total de números e a media aritmética de todos os números
da lista. '''

n = 0
l = []
c = 0
s = 0
n = int(input('n: '))
while n != 999:
    l.append(n)
    c += 1
    s += n
    n = int(input('n: '))
if c == 0:
    print('Você não digitou nenhum nº')
else:
    print(l)
    print(f'{c} números digitados')
    print(f'{s} é a soma de todos os números')
    print(f'{s/c} é a média entre eles')