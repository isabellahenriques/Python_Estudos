#Faça um algoritmo que leia o salario de um funcionário e mostre seu novo salário com 15% de aumento

salarioAtual = float(input("Digite o seu salário atual R$ "))
novoSalario = salarioAtual + (salarioAtual * 0.15)

print("O novo salário é R$ {}".format(novoSalario))
