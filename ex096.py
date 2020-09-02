''' Faça um programa que tenha uma função chamada área(),
que receba as dimensões de um terreno retangular (largura e comprimento)
e mostre a área do terreno.'''


def area(largura, comprimento):
    a = largura * comprimento
    print(f'A área de um terreno {largura}m X {comprimento}m é de {a} m².')


# Programa Principal
print("Controle de Tereenos")
print("-" * 20)
l = float(input("Largura (m): "))
c = float(input("Comprimento (m): "))
area(l, c)
