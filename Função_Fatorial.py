def fatorial(numero = 1):
    f = 1
    for contador in range(numero, 0, -1):
        f = f * contador
    return f


n = int(input("Digite um número para calcular o seu fatorial: "))
print(f'O fatorial de {n} é: {fatorial(n)}')
