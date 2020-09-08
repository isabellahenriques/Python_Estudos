from ex115.lib.interface import *
from ex115.lib.arquivo import *
from time import sleep

arq = "cursoemvideo.txt"

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(["VER PESSOAS CADASTRADAS",
                     "CADASTRAR NOVA PESSOA",
                     "SAIR DO SISTEMA"])
    if resposta == 1:
        #opção de listar o conteúdo de um arquivo!
        lerArquivo(arq)
    elif resposta == 2:
        #opção de cadastrar uma nova pessoa
        cabecalho("NOVO CADASTRO")
        nome = str(input("Nome: "))
        idade = leiaInt("Idade: ")
        cadastrar(arq, nome, idade)

    elif resposta == 3:
        #opção de sair do sistema
        cabecalho("Saindo do sistema...Até logo!")
        break
    else:
        #Digitou uma opção incorreta no menu.
        print("\033[31mERRO! Digite uma opção válida!\033[m")
    sleep(2)
