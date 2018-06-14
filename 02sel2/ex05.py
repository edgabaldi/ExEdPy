v1 = float(input('v1: '))
v2 = float(input('v2: '))
v3 = float(input('v3: '))
media1 = (v1 + v2 + v3) / 3
if media1 >= 7:
    print(f'Aprovado por Média!\nMédia {media1:.1f}')
else:
    menor = v1
    if v1 > v2 < v3:
        menor = v2
    elif v2 > v3 < v1:
        menor = v3
    print(f'Reprovado por Média! Média alcançada: {media1}\nFaça a Reposição.')
    reposicao = float(input('Nota da Reposição: '))
    media2 = (((v1 + v2 + v3) - menor) + reposicao) / 3
    if reposicao > menor:
        if media2 >= 7:
            print(f'Aprovado na Reposição!, Média alcançada: {media2:.1f}')
        else:
            print(f'Reprovado na Reposição, média alcançada: {media2:.1f}\nFaça a prova final.')
            prova_final = float(input('Nota da prova final: '))
            media3 = media2 + prova_final
            if media3 >= 12:
                print(f'Aprovado na prova final! Média alcançada: {media3:.1f}')
            else:
                print(f'Reprovado, média final alcançada {media3:.1f} é menor que 12')
    else:
        print(f'Reprovado na Reposição! Méida alcançada: {media2:.1f}')
