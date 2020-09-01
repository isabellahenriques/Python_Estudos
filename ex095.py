'''Aprimore o desafio 93 para que ele funcione com vários jogadores,
incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.'''
time = list()
jogador = dict()
partidas = list()

while True:
    jogador.clear()
    jogador["nome"] = str(input('Nome do Jogador: '))
    totalPartidas = int(input(f'Quantas partidas o {jogador["nome"]} jogou: '))
    partidas.clear()

    print()
    print("GOLS EM CADA PARTIDA")
    for contador in range(0,totalPartidas):
        partidas.append(int(input(f'Quantos Gols na {contador + 1}ª partida: ')))
    jogador["gols"] = partidas[:]
    jogador["total"] = sum(partidas)
    time.append(jogador.copy())

    while True:
        print()
        resposta = str(input("Quer continuar: [S/N] ")).upper()[0]
        print()
        if resposta in "SN":
            break
        print("Responta apenas S ou N.")
    if resposta == "N":
        break
print("=+" * 30)
print("cod ", end='')
for elemento in jogador.keys():
    print(f'{elemento:<15}', end="")
print()

print("-" * 40)
for chave, valor in enumerate(time):
    print(f'{chave:>3} ', end="")
    for dado in valor.values():
        print(f'{str(dado):<15}', end="")
    print()
print("-" * 40)
while True:
    busca = int(input("Mostrar dados de qual jogador: [999 para parar] "))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não exite jogador com código {busca}!')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}:')
        for indice, g in enumerate(time[busca]["gols"]):
            print(f'     No {indice + 1}º jogo fez {g} gols.')
    print("-" * 40)
print("<< Volte Sempre >>")

