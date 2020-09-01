'''Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA,
mostrando os 10 primeiros termos da progressão usando a estrutura while.'''
print("Gerador de PA")
primeiroTermo = int(input("Qual o primeiro Termo da PA: "))
razao = int(input("Qual a razão dessa PA: "))

termo = primeiroTermo
cont = 1

while cont <= 10:
    print("{} ->".format(termo), end=" ")
    termo = termo + razao
    cont = cont + 1
print("Fim")
