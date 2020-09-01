''' Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.'''
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somaPar = maiorValor = somaColuna = 0
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha},{coluna}]: '))
#print(matriz)
print("+=" * 30)
for linha in range(0,3):
    for coluna in range(0, 3):
        if matriz[linha][coluna] % 2 == 0:
            somaPar = somaPar + matriz[linha][coluna]
        print(f'[{matriz[linha][coluna]:^5}]', end="")
    print()
print("+=" * 30)
print(f'A soma dos valores PARES é {somaPar}.')
for linha in range(0, 3):
    somaColuna = somaColuna + matriz[linha][2]
print(f'A soma dos valores da 3ª coluna é {somaColuna}.')
for coluna in range(0, 3):
    if coluna == 0:
        maiorValor = matriz[1][coluna]
    elif matriz[1][coluna] > maiorValor:
        maiorValor = matriz[1][coluna]
print(f'O maior valor da 2ª linha é {maiorValor}.')
