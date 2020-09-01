print("------- CALCULADORA -------")
sair = False
while sair == False:
    numero1 = input("Digite o primeiro número: ")
    numero1 = int(numero1)
    operador = input("Digite o operador matemático (+ - / * ) : ")
    numero2 = input("Digite o segundo número: ")
    numero2 = int(numero2)
    # + soma
    if operador == "+":
        operacao = numero1 + numero2
    # - Subtração
    if operador == "-":
        operacao = numero1 - numero2
    # / divisão
    if operador == "/":
        operacao = numero1 / numero2
    # * multiplicação
    if operador == "*":
        operacao = numero1 * numero2
    print("Resultado: ")
    print(operacao)
    teste = input("Deseja sair (n/s): ")
    if teste == "s":
        sair = True
