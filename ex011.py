'''Faça um programa que leia a largura e a altura de uma parede em metros,
calcule sua área e a quantidade de tinta necessária para pintá-la,
sabendo que cada litro de tinta, pinta uma área de de 2m^2'''

largura = float(input("Qual a Largura da parede: "))
altura = float(input("Qual a altura da parede: "))
area = largura * altura
tinta = area/2

print("Sua parede tem a dimensão de {} x {} e sua área é de {} m²".format(largura, altura, area))
print("Para pintar essa parede, você vai precisar de {} litros de tinta.".format(tinta))
