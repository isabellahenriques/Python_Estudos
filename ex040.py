'''Crie um programa que leia duas notas de um aluno e calcule sua média,
mostrando uma mensagem no final, de acordo com a média atingida:
– Média abaixo de 5.0: REPROVADO
– Média entre 5.0 e 6.9: RECUPERAÇÃO
– Média 7.0 ou superior: APROVADO'''
nota1 = float(input("Qual a primeira nota: "))
nota2 = float(input("Qual a segunda nota: "))
media = (nota1 + nota2)/2
print("Tirando {:.1f} e {:.1f}, a média é {:.1f}".format(nota1, nota2, media))
if media < 5.0:
    print("O aluno está REPROVADO")
elif 5.0 <= media <= 6.9:
    print("O aluno está em RECUPERAÇÃO")
else:
    print("O aluno está APROVADO")

