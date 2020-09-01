''' A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento
de um atleta e mostre sua categoria, de acordo com a idade:
– Até 9 anos: MIRIM
– Até 14 anos: INFANTIL
– Até 19 anos: JÚNIOR
– Até 25 anos: SÊNIOR
– Acima de 25 anos: MASTER'''
from datetime import date
ano = int(input("Qual o ano de nascimento: "))
idade = date.today().year - ano
#print(idade)
if idade <= 9:
    print("Você tem {} anos, sua categoria é MIRIM".format(idade))
elif 9 < idade <= 14:
    print("Você tem {} anos, sua categoria é INFANTIL".format(idade))
elif 14 < idade <= 19:
    print("Você tem {} anos, sua categoria é JUNIOR".format(idade))
elif 19 < idade <= 25:
    print("Você tem {} anos, sua categoria é SENIOR".format(idade))
else:
    print("Você tem {} anos, sua categoria é MASTER".format(idade))
