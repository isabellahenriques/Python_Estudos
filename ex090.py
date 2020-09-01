'''Faça um programa que leia nome e média de um aluno,
guardando também a situação em um dicionário.
No final, mostre o conteúdo da estrutura na tela.'''
aluno = dict()

aluno['Nome'] = str(input("Nome: "))
aluno['Media'] = float(input(f'Média do {aluno["Nome"]}: '))
if aluno['Media'] >= 7:
    aluno['Situação'] = "Aprovado"
elif 5 <= aluno['Media'] < 7:
    aluno['Situação'] = "Recuperação"
else:
    aluno['Situação'] = "Reprovado"
print("=-" * 30)
for chave, valor in aluno.items():
    print(f'{chave} = {valor}')



