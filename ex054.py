'''Crie um programa que leia o ano de nascimento de sete pessoas.
No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.'''
from datetime import date
atual = date.today().year
totMaior = 0
totMenor = 0
for pessoas in range(1,8):
    anoDeNasc = int(input("Em que ano a {}ª pessoa nasceu: ".format(pessoas)))
    idade = atual - anoDeNasc
    if idade >= 21:
        #print("Maior de idade!")
        totMaior = totMaior + 1
    else:
        #print("Menor de idade")
        totMenor = totMenor + 1
print("Ao todo tivemos {} pessoas maiores de idade".format(totMaior))
print("Ao todo tivemos {} pessoas menores de idade".format(totMenor))
