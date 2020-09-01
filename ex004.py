'''Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e
todas as informações possíveis sobre ele.'''
a = input("Digite algo: ")
print(a)
print("O tipo primitivo desse valor é ",type(a))
print("Só tem espaços? ",a.isspace())
print("É um número? ",a.isnumeric())
print("É alfabetico? ",a.isalpha())
print("É alfanumerico? ",a.isalnum())
print("Esta em maiuscula? ",a.isupper())
print("Esta em minuscula? ",a.islower())
print("Esta em capitalizado? ",a.istitle())
