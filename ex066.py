'''Crie um programa que leia números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999,
que é a condição de parada. No final, mostre quantos números foram digitados
e qual foi a soma entre elas (desconsiderando o flag).'''
numero = soma = cont = 0
while True:
    numero = int(input("Digite um número [999 para parar]: "))
    if numero == 999:
        break
    soma = soma + numero
    cont = cont + 1
print(f"A soma vale {soma} e foram digitados {cont} números")

