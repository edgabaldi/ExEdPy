''' – Calcular a quantidade necessária de latas de tinta para pintar uma parede de L m de
largura por H m de altura. Considerando que o consumo de tinta e’ de 3L por metro
quadrado e a quantidade de tinta por lata e’ 2L'''
from math import ceil
l = float(input('Largura da parede (em metros): '))
h = float(input('altura da parrede (em metros): '))
parede = l * h
litros = parede * 3
latas = ceil(litros / 2)
print(f'A parede tem {parede:.2f}m²')
print(f'Serão necessários {litros:.2f} litros de tinta')
print(f'Para isso é necessário {latas} latas de tinta')
