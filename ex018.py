#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo
import math
angulo = float(input("Qual o valor do angulo: "))
seno = math.sin(math.radians(angulo))
print("O ângulo de {} tem SENO de {:.2f}".format(angulo, seno))
coseno = math.cos(math.radians(angulo))
print("O ângulo de {} tem COSSENO de {:.2f}".format(angulo, coseno))
tangente = math.tan(math.radians(angulo))
print("O ângulo de {} tem TANGENTE de {:.2f}".format(angulo, tangente))


