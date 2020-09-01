'''Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar ou não.
No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato
'''
print("-" * 32)
print("LOJA SUPER BARATÃO")
print("-" * 32)
total = 0
totMil = 0
menorPreco = 0
contador = 0
barato = " "
while True:
    produto = str(input("Nome do produto: "))
    preco = float(input("Preco R$ "))
    contador = contador + 1
    total = total + preco
    if preco > 1000:
        totMil = totMil + 1
    if contador == 1:
        menorPreco = preco
        barato = produto
    else:
        if preco < menorPreco:
            menorPreco = preco
            barato = produto
    continuar = " "
    while continuar not in "SN":
        continuar = str(input("Quer continuar: [S/N] ")).upper()[0].strip()
    if continuar == "N":
        break
print("-" * 8 + "FIM DO PROGRAMA" + "-" * 8)
print(f"O total de compras foi R$ {total:.2f}")
print(f"Temos {totMil} produtos custando mais de R$ 1000.00")
print(f"O produto mais barato foi {barato} que custou R$ {menorPreco:.2f}")
