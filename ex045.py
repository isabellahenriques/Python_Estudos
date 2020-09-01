#Crie um programa que faça o computador jogar Jokenpô com você.
from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
#print("o computador escolheu: {}".format(itens[computador]))
print("{:=^25}".format(" JOKENPO "))
print('''Suas opções
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input("Qual é a sua jogada? "))

print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO!!!!!!!")
sleep(1)
print('-=' * 12)
if computador == 0:#pedra
    if jogador == 0:
        print("EMPATE!")
    elif jogador == 1:
        print("JOGADOR VENCEU!")
    elif jogador == 2:
        print("COMPUTADOR VENCEU!")
    else:
        print("JOGADA INVALIDA!")
elif computador == 1:#papel
    if jogador == 0:
        print("COMPUTADOR VENCEU!")
    elif jogador == 1:
        print("EMPATE")
    elif jogador == 2:
        print("JOGADOR VENCEU!")
    else:
        print("JOGADA INVALIDA!")
elif computador == 2:#tesoura
    if jogador == 0:
        print("JOGADOR VENCEU!")
    elif jogador == 1:
        print("COMPUTADOR VENCEU!")
    elif jogador == 2:
        print("EMPATE")
    else:
        print("JOGADA INVALIDA!")

print('-=' * 12)
print("Computador jogou {}".format(itens[computador]))
print("Jogador jogou {}".format(itens[jogador]))
print('-=' * 12)

