''' 2 – Projete um algoritmo para ler uma lista de números terminada pelo numero 999 e
mostrar cada numero lido. Ao final o algoritmo deve mostrar o total de números lidos e a
média aritmética de todos os números da lista. Observar que o número 999 é somente o
indicador de final dos números, ele não entra na contagem e nem no cálculo da média. '''

l = []
c = s = m = 0

while True:
    n = int(input('n: '))
    if n == 999:
        break
    else:
        l.append(n)
        s += n
        c += 1
if  c != 0:
    print(f'Lidos: {l}')
    print(f'Qauntidade de lidos: {c}')
    print(f'Média: {s/c}')
else:
    print('Nenhum número digitado')