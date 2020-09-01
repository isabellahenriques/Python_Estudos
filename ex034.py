'''Escreva um programa que pergunte o salário de um funcionário e
calcule o valor do seu aumento. Para salários superiores a R$1250,00
calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.'''
salario = float(input("Qual o salário do funcionário? R$ "))
if salario >= 1250:  # Aumento de 10%
    #novoSalario = salario * 0.1 + salario
    print("Quem ganhava R$ {:.2f} passa a ganhar R$ {:.2f} agora.".format(salario, salario * 0.1 + salario))
else:  # Aumento de 15%
    #novoSalario = salario * 0.15 + salario
    print("Quem ganhava R$ {:.2f} passa a ganhar R$ {:.2f} agora.".format(salario, salario * 0.15 + salario))
