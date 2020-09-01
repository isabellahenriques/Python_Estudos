'''Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.'''
contagem = ("zero", "um", "dois", "tres","quatro",
            "cinco", "seis", "sete", "oito", "nove",
            "dez", "onze", "doze", "treze", "catorze",
            "quinze", "desesseis", "dezessete", "dezoito",
            "dezenove", "vinte")
while True:
    numero = int(input("Digite um numero entre 0 e 20: "))
    if 0 <= numero <= 20:
        break
    print("Tente novamente. ", end="")
print(f"Voce digitou o numero {contagem[numero]}.")
