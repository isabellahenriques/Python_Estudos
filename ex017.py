'''Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retânguilo
Calcule e mostre o comprimento da hipotenusa'''


'''co = float(input("Digite o comprimento do cateto oposto do triangulo: "))
ca = float(input("Digite o comprimento do cateto adjacent do triangulo: "))
hi= (co ** 2 + ca ** 2) ** (1/2)
print("A hipotenusa vai medir {:.2f}".format(hi))'''

'''import math
co = float(input("Digite o comprimento do cateto oposto do triangulo: "))
ca = float(input("Digite o comprimento do cateto adjacent do triangulo: "))
hi = math.hypot(co, ca)
hi= (co ** 2 + ca ** 2) ** (1/2)
print("A hipotenusa vai medir {:.2f}".format(hi))'''

from math import hypot
co = float(input("Digite o comprimento do cateto oposto do triangulo: "))
ca = float(input("Digite o comprimento do cateto adjacent do triangulo: "))
hi = hypot(co, ca)
print("A hipotenusa vai medir {:.2f}".format(hi))
