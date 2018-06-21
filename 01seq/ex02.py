''' – Calcular a quantidade necessária de latas de tinta para pintar uma parede de L m de
largura por H m de altura. Considerando que o consumo de tinta e’ de 3L por metro
quadrado e a quantidade de tinta por lata e’ 2L'''

def qtde_latas_tinta(largura, altura):
    parede = largura * altura
    litros = parede * 3
    qtde_latas = litros / 2
    return qtde_latas


#
# Teste 1
#

resposta = qtde_latas_tinta(10, 3)
esperado = 45

assert resposta == esperado, resposta
