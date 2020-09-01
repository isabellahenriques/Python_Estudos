'''Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
No final, mostre os 10 primeiros termos dessa progressão.'''
primeiroTermo = int(input("Qual o primeiro Termo da PA: "))
razao = int(input("Qual a razão dessa PA: "))
decimo = primeiroTermo + (10 - 1) * razao
for c in range(primeiroTermo,decimo + razao,razao):
    print("{}".format(c), end=" -> ")
print("FIM")

