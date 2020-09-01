'''Crie um programa que leia a idade e o sexo de várias pessoas.
A cada pessoa cadastrada, o programa deverá perguntar
se o usuário quer ou não continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos.
'''
print("=+" * 15)
print("Cadastrar uma pessoa")
print("=+" * 15)
tot18 = 0
homens = 0
mulheres = 0
while True:
    idade = int(input("Idade: "))
    sexo = " "
    while sexo not in "MF":
        sexo = str(input("Sexo [M/F]: ")).upper()[0].strip()
    if idade >= 18:
        tot18 = tot18 + 1
    if sexo == "M":
        homens = homens + 1
    if sexo == "F" and idade < 20:
        mulheres = mulheres + 1
    continuar = " "
    while continuar not in "SN":
        continuar = str(input("Quer continuar: [S/N] ")).upper()[0].strip()
    if continuar == "N":
        break
print(f"Total de pessoas com mais de de 18 anos: {tot18}")
print(f"Total de Homens cadastrados: {homens}")
print(f"Total de Mulheres cadastradas com menos de 20 anos: {mulheres}")
