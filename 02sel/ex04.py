'''4 – Ler 4 números (Opção, N1, N2, N3) e mostrar o valor de N1 se a Opção for igual a 2; O
valor de N2 se a opção for igual a 3 e o valor de N3, se Opção for igual a 4. Os únicos
valores possíveis para a variação de Opção são 2, 3 e 4. '''

i = 0
lista = []
for i in range(1, 4):
    n = int(input(f'digdite o {i}º número: '))
    i += 1
    lista.append(n)
opção = str(input(''' 
Escolha qual nº quer ver novamente:

[2] para ver o 1º número
[3] para ver o 2º número
[4] para ver o 3º número

'''))

while opção not in '234':
    opção = str(input('''
OPÇÃO INVÁLIDA.
Utilize apenas as opções abaixo:
[2] para ver o 1º número
[3] para ver o 2º número
[4] para ver o 3º número
'''))

print(f'Você escolheu a opção: {opção}')
print(f'Vovê escolheu ver o nº: {lista[(int(opção)-2)]}')


