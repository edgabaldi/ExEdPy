''' 4 – Projete um algoritmo para ler o nome e a idade de várias pessoas e classificá-las de
acordo com a faixa etária: (< ou = a 12: criança, 13 – 18: adolescente, > 18 adulto). O
algoritmo termina quando o nome for igual a ‘fim’. O algoritmo deve mostrar o nome, a idade
e a faixa etária de cada pessoa lida. '''

n = f = ''
c = 0
ln = []
li = []
lf = []
while True:
    n = str(input('Nome: ')).strip().upper()
    if n == 'FIM':
        break
    i = int(input('Idade: '))
    c += 1
    if i <= 12:
        f = 'Criança'
    elif i <= 18:
        f = 'Adolescente'
    else:
        f = 'Adulto'
    ln.append(n)
    li.append(i)
    lf.append(f)
print('')
print(f'{"NOME":^12}', end='')
print(f'{"IDADE":^12}',end='')
print(f'{"FAIXA ETÁRIA":^12}')
for c in range(0, c):
    print(f'{ln[c]:^12}', end=' ')
    print(f'{li[c]:^12}', end=' ')
    print(f'{lf[c]:^12}')
