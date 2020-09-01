#Faça um algoritmo que leia o preço de um produto e mostre o seu novo preço com 5% de desconto.

precoAtual = float(input("Qual o valor do produto R$ "))
precoNovo = precoAtual - (precoAtual * 0.05)

print("O novo preço é R$ {:.2f}".format(precoNovo))
