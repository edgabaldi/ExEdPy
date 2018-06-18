''' 3 - Projete um algoritmo para ler vários valores de temperatura em graus Celsius e converte-los para graus Fahrenheit. O algoritmo deve mostrar a temperatura em graus Celsius e a correspondente temperatura em graus Fahrenheit. O algoritmo encerra quando a temperatura em graus Celsius for igual a 999.'''

c = int(input('ºC: '))

while c != 999:
    f = ((9 * c) + 160) / 5
    print(f' {c}ºC  =  {f}ºF')
    c = int( input( '\nºC: ' ) )