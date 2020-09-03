def par(numero=0):
    if numero % 2 == 0:
        return True
    else:
        return False


num = int(input("Digite um número para saber se é PAR ou IMPAR: "))
if par(num):
    print(f"O número {num} é PAR!")
else:
    print(f"O número {num} é IMPAR!")

