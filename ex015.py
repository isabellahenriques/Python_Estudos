'''Escreva um programa que pergunte a quantidade de km percorridos por um carro aludado
e a quantidade de dias pelos quais ele foi alugado.
Calcule o preço a pagar sabendo que o carro custa R$60.00 por dia e R$0.15 por km rodado.'''

dias = int(input("Quantos dias você ficou com o carro: "))
km = float(input("Quantos km você rodou com o carro: "))
valorKm = (km * 0.15)
valorDias = (dias * 60)
total = valorKm + valorDias  #total = (km * 0.15) + (dias * 0.60)

print("Você vai pagar R${:.2f}".format(total))
