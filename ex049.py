'''Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher,
só que agora utilizando um laço for.'''
n = int(input("Digite um número para a tabuada: "))
for contador in range(1,11):
    tabuada = contador * n
    print("{} x {} = {}".format(n,contador,tabuada))


