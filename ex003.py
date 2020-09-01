#Crie um programa que leia dois números e mostre a soma entre eles.
n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
soma = (n1 + n2)

#print("A soma vale ", soma)
#print("A soma entre ",n1, " e ",n2," vale ",soma)
print("A soma entre {} e {} vale {}".format(n1, n2, soma))
