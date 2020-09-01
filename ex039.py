'''Faça um programa que leia o ano de nascimento de um jovem e informe,
de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar,
se é a hora exata de se alistar ou se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.'''
from datetime import date
ano = int(input("Em que ano você nasceu? "))
atual = date.today().year
idade = date.today().year - ano
print("Quem nasceu em {} tem {} anos em {}.".format(ano,idade,atual))
if idade == 18:
    print("É hora de se alistar")
elif idade >= 18:
    print("Já se passaram {} anos do alistamento".format(idade-18))
else:
    print("Faltam {} anos para alistar".format(18-idade))

