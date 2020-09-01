print("=+" *21)
print("Conversor de NÚMRTO INTEIRO para BINARIO")
print("=+" *21)

numeroInicial = int(input("Digite um número inteiro: "))
numeroInformado = numeroInicial
numeroBinario = ""

while numeroInicial > 0:
    numeroBinario += str(numeroInicial % 2)
    numeroInicial = int(numeroInicial/2)
print(f"O numero inteiro {numeroInformado} em binário é {numeroBinario[::-1]}")
