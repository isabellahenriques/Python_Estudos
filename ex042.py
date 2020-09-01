'''Refaça o DESAFIO 35 dos triângulos,
acrescentando o recurso de mostrar que tipo de triângulo será formado:
– EQUILÁTERO: todos os lados iguais
– ISÓSCELES: dois lados iguais, um diferente
– ESCALENO: todos os lados diferentes'''
l1 = float(input("Digite o lado 1: "))
l2 = float(input("Digite o lado 2: "))
l3 = float(input("Digite o lado 3: "))
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print("Pode formar um Triângulo",end='')
    if (l1 == l2) and (l1 == l3):
        print(" EQUILÁTERO!")
    elif (l1 == l2) or (l1 == l3) or (l2 == l3):
        print(" ISOCELES!")
    elif (l1 != l2) or (l1 != l3) or (l2 != l3):
        print(" ESCALENO!")
else:
    print("Não pode formar um Triângulo!")



