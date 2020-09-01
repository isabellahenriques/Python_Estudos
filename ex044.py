'''Elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu preço normal e condição de pagamento:
– à vista dinheiro/cheque: 10% de desconto
– à vista no cartão: 5% de desconto
– em até 2x no cartão: preço formal
– 3x ou mais no cartão: 20% de juros'''
print("{:=^40}".format(" LOJAS GUANABARA "))
preco = float(input("Preço das compras R$ "))
print("FORMAS DE PAGAMENTO")
print("[ 1 ] à vista Dinheiro\Cheque")
print("[ 2 ] à vista no Cartão")
print("[ 3 ] 2x no Cartão")
print("[ 4 ] 3x no Cartão")
opcao = int(input("Qual é a opção: "))
if opcao == 1:
    print("Sua compra de R${:.2f} vai custar R${:.2f} no final".format(preco,(preco - preco * 10/100)))
elif opcao == 2:
    print("Sua compra de R${:.2f} vai custar R${:.2f} no final".format(preco,(preco - preco * 5/100)))
elif opcao == 3:
    print("Sua compra de R${:.2f} sera parcelada em 2x sem juros.\nO valor de cada parcela será R${:.2f}.".format(preco, preco/2))
elif opcao == 4:
    parcelas = int(input("Quantas parcelas: "))
    precoFinal = preco + (preco * 20/100)
    print("Sua compra sera parcelada em {}x de R${:.2f} COM JUROS.".format(parcelas,precoFinal/parcelas))
    print("Sua compra de R${:.2f} vai custar R${:.2f} no final.".format(preco, precoFinal))
else:
    print("Opção invalida, tente novamente")


