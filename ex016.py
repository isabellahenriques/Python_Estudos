#Crie um programa que leia um numero real qualquer pelo teclado e mostre na tela a sua porção inteira

from math import trunc
n = float(input("Digite um número real: "))
print("O número digitado foi {} e sua parte inteira é {}". format(n, trunc(n)))

'''n = float(input("Digite um número real: "))
i = n // 1
print("O número digitado foi {} e sua parte inteira é {}". format(n, i))'''

'''n = float(input("Digite um número real: "))
print("O número digitado foi {} e sua parte inteira é {}.". format(n, int(n)))'''
