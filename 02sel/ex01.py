'''1 - Ler dois números e indicar se são iguais, ou se diferentes, mostrar o maior e o menor
(nesta ordem) '''
n1 = int(input('nº: '))
n2 = int(input('nº: '))
maior = menor = n1
if n2 > n1:
    maior = n2
    print( f'O segundo nº, {n2}, é  maior que o primeiro, {n1}.')
elif n1 == n2:
    print('Os dois números são iguais')
else:
    print(f'O primeiro nº, {n1}, é  maior que o segundo, {n2}.')