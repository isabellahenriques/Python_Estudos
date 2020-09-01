'''Faça um programa que mostre a tabuada de vários números,
um de cada vez, para cada valor digitado pelo usuário.
O programa será interrompido quando o número solicitado for negativo.'''
while True:
    numero = int(input("Digite um número para a tabuada: "))
    if numero < 0:
            break
    print("-" * 30)
    for contador in range(1,11):
        print(f"{numero} x {contador} = {contador * numero}")
    print("-" * 30)
print("-" * 30)
print("Acabou!")
print("-" * 30)
