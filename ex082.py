'''Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os valores pares
e os valores ímpares digitados, respectivamente.
Ao final, mostre o conteúdo das três listas geradas.'''
numero = list()
par = list()
impar = list()
while True:
    n = int(input("Digite um valor: "))
    if n not in numero:
        numero.append(n)
        if n % 2 == 0:
            par.append(n)
        else:
            impar.append(n)
    else:
        print("Valor duplicado! Não adicionado!")
    resposta = str(input("Quer continuar? [S/N] ")).upper().strip()
    if resposta in "N":
        break
print("=+" * 30)
print(f'Você digitou os valores {numero}')
print(f'Os valores pares sao {par}')
print(f'Os valores impares sao {impar}')
