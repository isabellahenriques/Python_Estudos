'''Faça um programa que leia três números e mostre qual é o maior e qual é o menor.'''

a = int(input("Primeiro valor: "))
b = int(input("Segundo valor: "))
c = int(input("Terceiro valor: "))
# menor valor
if a < b and a < c:
    menor = a
if b < c and b < a:
    menor = b
if c < a and c < b:
    menor = c
# maior valor
if a > b and a > c:
    maior = a
if b > c and b > a:
    maior = b
if c > a and c > b:
    maior = c

print("O menor valor digitado foi {} e o maior valor digitado foi {} ".format(menor, maior))
