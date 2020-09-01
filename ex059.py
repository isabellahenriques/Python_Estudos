'''Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.'''
from time import sleep
n1 = int(input("Primeiro Valor: "))
n2 = int(input("Segundo Valor: "))
opcao = 0
while opcao != 5:
    print('''    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa''')
    opcao = int(input("Qual a sua opção: "))
    if opcao == 1:
        soma = n1 + n2
        print("{} + {} = {}".format(n1, n2, soma))
    elif opcao == 2:
        multiplicar = n1 * n2
        print("{} * {} = {}".format(n1, n2, multiplicar))
    elif opcao == 3:
        if n1 > n2:
            print("{} é maior".format(n1))
        elif n1 < n2:
            print("{} é maior".format(n2))
        else:
            print("Os dois números são iguais")
    elif opcao == 4:
        print("Informe os números novamente: ")
        n1 = int(input("Primeiro Valor: "))
        n2 = int(input("Segundo Valor: "))
    elif opcao == 5:
        print("Finalizando...")
    else:
        print("Opção inválida, tente novamente!")
    print("=-=" * 12)
    sleep(1)
print("Fim do programa. Volte Sempre!!!")
