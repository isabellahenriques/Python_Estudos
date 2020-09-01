#Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.
#n = int(input("Digite um número: "))
#s = n + 1
#a = n - 1
#print("o sucessor de ", n , "é", s , "e seu antecessor é", a)
#print("Analisando o valor {}, seu antecessor é {} e seu sucessor é {}".format(n, a, s))

n = int(input("Digite um número: "))
print("Analisando o valor {}, seu antecessor é {} e seu sucessor é {}".format(n, (n-1), (n+1)))
