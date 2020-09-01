'''Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.'''
numero = list()
while True:
    n = int(input("Digite um valor: "))
    if n not in numero:
        numero.append(n)
    else:
        print("Valor duplicado! Não adicionado!")
    resposta = str(input("Quer continuar? [S/N] ")).upper().strip()
    if resposta in "N":
        break
print("=+" *30)
print(f'Você digitou {len(numero)} elementos.')
print(f'Você digitou os valores {numero}')
numero.sort()
print(f'Os valores em ordem crescente são: {numero}')
numero.sort(reverse=True)
print(f'Os valores em ordem decrescente são: {numero}')
if 5 in numero:
    print("O valor 5 foi digitado.")
else:
    print("O valor 5 não foi digitado.")



