''' 1 – Projete um algoritmo para ler uma lista de números terminada pelo numero 0 e mostrar
cada numero lido. Ao final o algoritmo deve mostrar o total de números lidos e a média
aritmética de todos os números da lista. Observar que o número 0 é somente o indicador de
final dos números, ele não entra na contagem e nem no cálculo da média. '''

l = []
c = s = 0

while True:
    n = int( input( 'n: ' ))
    if n == 0:
        break
    l.append(n)
    c += 1
    s += n
if c != 0:
    print(f'Números digitados: {l}')
    print(f'Total de númeroos lidos: {c}')
    print(f'Média aritmética {s/c}')
else:
    print('Nenhum número digitado')