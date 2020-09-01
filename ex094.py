'''Crie um programa que leia nome, sexo e idade de várias pessoas,
guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média'''
galera = list()
pessoa = dict()
soma = media = 0
while True:
    pessoa.clear()
    pessoa["nome"] = str(input("Nome: "))
    while True:
        pessoa["sexo"] = str(input("Sexo: [M/F] ")).upper()[0]
        if pessoa["sexo"] in "MF":
            break
        print("ERRO! Por favor, digite apenas M ou F.")
    pessoa["idade"] = int(input("Idade: "))
    soma = soma + pessoa["idade"]
    galera.append(pessoa.copy())
    while True:
        resposta = str(input("Quer continuar? [S/N] ")).upper()[0]
        if resposta in "SN":
            break
        print("ERRO! Por favor, digite apenas S ou N.")
    if resposta == "N":
        break
print("=+" * 30)
print(f'A) Ao todo temos {len(galera)} pessoas cadastradas.')
media = soma / len(galera)
print(f'B) A média de idade é de {media:5.2f} anos.')
print(f'c) As mulheres cadastradas foram ', end="")
for p in galera:
    if p["sexo"] in "Ff":
        print(f'{p["nome"]} ',end="")
print()
print("D) Listas das pessoas que estão acima da média: ")
for p in galera:
    if p["idade"] >= media:
        print("     ")
        for chave, valor in p.items():
            print(f'{chave} = {valor}; ', end="")
        print()
print("Finalizado!")
