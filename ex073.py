''':Exercício Python 73: Crie uma tupla preenchida com os
20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol,
na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da Chapecoense.'''
times = ("corinthias", "palmeiras", "santos", "grêmio",
         "cruzeiro", "flamengo", "vasco", "chapecoense",
         "atletico", "botafogo", "atletico-pr", "bahia",
         "são paulo", "fluminense", "sport recife", "ex vitoria",
         "coritiba","avai", "ponte preta", "atletico-go")
print("-=" *15)
print(f'lista de times: {times}')
#for t in times:
#    print(t)
print("-=" *15)
print(f'Os 5 primeiros são {times[0:5]}')
print("-=" *15)
print(f'Os 4 ultimos são: {times[-4:]}')
print("-=" *15)
print(f'Times em ordem alfabética {sorted(times)}')
print("-=" *15)
print(f'Chapecoense está na {times.index("chapecoense")+1}ª posicão')
