'''Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e
mostre quantos dólares ela pode comprar.'''

real = float(input("Quantos reais você tem: R$ "))
dolar = real / 3.27

print("Você pode comprar US$ {:.2f} dolares.".format(dolar))
