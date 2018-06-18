''' 5 - Projete um algoritmo para ler a placa e o ano de fabricação de vários carros e classificálas
de acordo com a seguinte tabela: (antes de 1994: fora de linha, de 1994 a 2003: usado,
de 2004 a 2008: semi-novo, > 2009 novo). O algoritmo termina quando a placa for igual a
‘ZZZ9999’. Caso o ano de fabricação seja menor que 1885 ou maior que 2010 deve ser
emitida a mensagem ‘ano inválido’ e solicitar novamente o ano. O algoritmo deve mostrar a
placa do carro, o ano de fabricação e a classificação de cada carro lido. '''


cls = ''
c = 0
lp = []
la = []
lc = []

while True:
    placa = str(input('\nPlaca: ')).strip().upper()
    if placa == 'ZZZ9999':
        break
    ano = int(input('Ano de fabricação: '))
    while ano < 1985 or ano > 2010:
        ano = int(input('Ano inválido!\nDidite o ano novamente: '))
    else:
        if ano < 1994:
            cls = 'Fora de linha'
        elif 1994 <= ano <= 2003:
            cls = 'Usado'
        elif 2004 <= ano <= 2008:
            cls = 'Semi-novo'
        else:
            cls = 'Novo'

        lp.append(placa)
        la.append(ano)
        lc.append(cls)
        c += 1

for c in range(0, c):
    print(lp[c], end=': ')
    print(la[c], end=' - ')
    print(lc[c])
