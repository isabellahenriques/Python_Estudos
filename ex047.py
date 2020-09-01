#Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.
print("Números Pares")
for contador in range(2, 51, 2):
    print(contador, end=" ")
print("\nFIM")


print("\nNúmeros Pares")
for contador in range(2, 51, 2):
    if contador % 2 == 0:
        print(contador, end=" ")
print("\nFIM")
