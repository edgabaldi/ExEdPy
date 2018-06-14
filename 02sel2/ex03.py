'''. Desenvolva um programa que recebe do usuário o placar de um jogo de futebol (os gols de cada
time) e informa se o resultado foi um empate, a vitória do primeiro time ou do segundo time.'''
gt1 = int(input('Gol(s) do 1º time: '))
gt2 = int(input('Gol(s) do 2º time: '))

if gt1 > gt2:
    print(f'''
O 1º Gahou!!!
[Time 1] {gt1} x {gt2} [Time 2]''')
elif gt1 < gt2:
    print(f'''
O 2º Gahou!!!
[Time 1] {gt1} x {gt2} [Time 2]''')
else:
    print(f'''
Empate
[Time 1] {gt1} x {gt2} [Time2]''')