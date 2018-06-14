'''Ler uma temperatura em graus centígrados e apresenta-la convertida em graus
Farenheit, a formula de conversão e’: F = ( 9 * C + 160) / 5, onde F e’ a temperatura em
Farenheit e C a temperatura em Centígrados.'''

TC = int(input('Temperatura em  Graus Centígrados: '))
TF = ((9 * TC) + 160) / 5
print(f'{TC}ºC é igual a {TF:.2f}ºF')






