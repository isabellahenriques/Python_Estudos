'''Crie um programa onde o usuário possa digitar vários valores numéricos e
cadastre-os em uma lista.
Caso o número já exista lá dentro, ele não será adicionado.
No final, serão exibidos todos os valores únicos digitados, em ordem crescente'''
numero = list()
while True:
    n = int(input("Digite um valor: "))
    if n not in numero:
        numero.append(n)
        print("Valor adicionado!")
    else:
        print("Valor duplicado! Não adicionado!")
    resposta = str(input("Quer continuar? [S/N] ")).upper().strip()
    if resposta in "N":
        break
print("=+" *30)
numero.sort()
print(f'Você digitou os valor {numero}')

