'''Faça um programa que leia um número qualquer e mostre o seu fatorial.
Exemplo: 5! = 5 x 4 x 3 x 2 x 1 = 120'''
from math import factorial
'''numero = int(input("Digite um número para o seu fatorial: "))
fatorial = factorial(numero)
print("{}! = {}".format(numero,fatorial))'''

numero = int(input("Digite um número para o seu fatorial: "))
c = numero
print('{}! = '.format(numero), end=" ")
fatorial = factorial(numero)
while c > 0:
    print("{}".format(c), end=" ")
    print(" x " if c > 1 else " = {}".format(fatorial), end=" ")
    c = c - 1

