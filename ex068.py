''' Faça um programa que jogue par ou ímpar com o computador.
O jogo só será interrompido quando o jogador perder,
mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.'''
from random import randint
print("=+" * 20)
print("Vamos jogar Par ou Impar")
print("=+" * 20)

numeroJogador = int(input("Digite um valor entre 0 e 10: "))
jogador = str(input("Par ou Ímpar? [P/I]: ")).upper().strip()[0]
computador = randint(0,10)
jogada = numeroJogador + computador

print(f"O computador escolheu: {computador}")
print(f"O jogador escolheu: {numeroJogador}")
print(f"A soma é {numeroJogador} + {computador} = {jogada}")

if (jogada % 2 == 0) and jogador == "P":
    print("Deu PAR - Você ganhou!")
elif (jogada % 2 == 0 ) and jogador == "I":
    print("DEU PAR - Você perdeu!")
elif (jogada % 2 != 0) and jogador == "I":
    print("DEU ÍMPAR - Você Ganhou!")
else:
    print("DEU ÍMPAR - Você perdeu!")
            











