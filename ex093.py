'''Crie um programa que gerencie o aproveitamento de um jogador de futebol.
O programa vai ler o nome do jogador e quantas partidas ele jogou.
Depois vai ler a quantidade de gols feitos em cada partida.
No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.'''
jogador = dict()
partidas = list()
jogador["nome"] = str(input('Nome do Jogador: '))
totalPartidas = int(input(f'Quantas partidas o {jogador["nome"]} jogou: '))
print("GOLS EM CADA PARTIDA")
for contador in range(0,totalPartidas):
    partidas.append(int(input(f'    Quantos Gols na {contador + 1}ª partida: ')))
jogador["gols"] = partidas[:]
jogador["total"] = sum(partidas)
print("=-" * 30)
print(jogador)
for chave, valor in jogador.items():
    print(f'O campo {chave} tem o valor {valor}')
print("=-" * 30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for indice, valor in enumerate(jogador['gols']):
    print(f'    => na {indice}ª partida, fez {valor} gols.')
print(f'Foi um total de {jogador["total"]} gols.')
