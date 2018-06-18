'''4º - Em 2008 o Sol atingiu sua atividade mínima apresentando praticamente sem suas
manchas. Em média em 11 anos ele atingirá sua atividade máxima. Ciclicamente ele
volta ao mínimo a cada 22 anos. Projete um algoritmo que calcule e imprima os anos
de mínima e máxima atividades solares até o ano de 2100'''

ano = 2008
print('MÁXIMA    MÍNIMA')
while ano < 2100:
    ano += 11
    print(ano, end='       ')
    ano += 22
    if ano < 2100:
        print(ano)
