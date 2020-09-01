'''Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade)
em um dicionário. Se por acaso a CTPS for diferente de ZERO,
o dicionário receberá também o ano de contratação e o salário.
Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.'''
from datetime import datetime
dados = dict()
dados["Nome"] = str(input("Nome: "))
AnoNascimento = int(input("Ano de Nascimento: "))
dados["Idade"] = datetime.now().year - AnoNascimento
dados["CTPS"] = int(input("Carteira de Trabalho (0 não tem): "))

if dados ["CTPS"] != 0:
    dados["contratação"] = int(input("Ano de Contratação: "))
    dados["salario"] = float(input("Salário R$ "))
    dados["Aposentadoria"] = dados["Idade"] + (dados["contratação"] + 35) - datetime.now().year
print("=-" * 30)
for chave, valor in dados.items():
    print(f'  - {chave} tem o valor: {valor}')
