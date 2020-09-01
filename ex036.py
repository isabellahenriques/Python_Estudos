'''Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.'''
preco = float(input("Qual o valor da casa? R$ "))
salario = float(input("Qual o salário do comprador? R$"))
anos = int(input("Quantos anos de financiamento? "))
prestacao = preco / (anos * 12)
#print("{:.2f}".format(prestacao))
#print("{:.2f}".format(salario * 30/100))
if prestacao >= (salario * 30/100):
    print("Para pagar um imovel de R$ {:.2f} em {} anos a prestação será de R$ {:.2f}.\nEmpréstimo NEGADO!".format(preco,anos,prestacao))
else:
    print("Para pagar um imovel de R$ {:.2f} em {} anos a prestação sera de R$ {:.2f}.\nEmpréstimo APROVADO!".format(preco,anos,prestacao))







