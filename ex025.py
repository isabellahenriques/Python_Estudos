#Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.
nome = str(input("Qual o seu nome completo: ")).strip()
#nomeCompl = nome.upper()
#print("SILVA" in nomeCompl)
#print("Seu nome tem Silva? {}".format("SILVA" in nomeCompl))

print("Seu nome tem Silva? {}".format("SILVA" in nome.upper()))

