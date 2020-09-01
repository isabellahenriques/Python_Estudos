''' Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados
e vai sortear 6 números entre 1 e 60 para cada jogo,
cadastrando tudo em uma lista composta.'''
from random import randint
from time import sleep
lista = list()
jogos = list()
print("-" * 35)
print(f'        JOGA NA MEGA SENA       ')
print("-" * 35)
quantidadeJogos = int(input("Quantos jogos você quer que eu sorteie? "))
totalJogos = 1
while totalJogos <= quantidadeJogos:
    contador = 0
    while True:
        numero = randint(1, 60)
        if numero not in lista:
            lista.append(numero)
            contador = contador + 1
        if contador > 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    totalJogos = totalJogos + 1
#print(f'Os números sorteados foram {jogos}')
print()
print("-=" * 3,f' SORTEADO {quantidadeJogos} JOGOS ', "-=" * 3)
print()
for indice, lista in enumerate(jogos):
    print(f'Jogo {indice + 1}: {lista}')
    sleep(1)
print("-=" * 5, "BOA SORTE", "-=" * 5)

