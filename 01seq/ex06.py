'''6 - Calcular o preço final de um automóvel cujo valor é calculado pela soma do preço de
fábrica com o preço dos impostos (45% do preço de fábrica) e a percentagem do revendedor
(28% do preço de fábrica).'''

preco_fabrica = int(input('Preço de frábrica: '))
imposto = preco_fabrica * 0.45
perc_revendedor = preco_fabrica * 0.28

print(f'Valor total: $ {(preco_fabrica + imposto + perc_revendedor):.2f}')
print(f'Imposto: $ {imposto:.2f}\nComissão do vendedor $ {perc_revendedor:.2f} ')

