'''Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
o primeiro que indique o número a calcular e outro chamado show,
que será um valor lógico (opcional) indicando se será mostrado
ou não na tela o processo de cálculo do fatorial.'''


def fatorial(n, show=False):
    """
    -> Calcula o Fatorial de um número,
    :param n: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número n.
    """
    f = 1
    for contador in range(n, 0, -1):
        if show:
            print(contador, end='')
            if contador > 1:
                print(f' x ', end='')
            else:
                print(' = ', end='')
        f = f * contador
    return f


#Programa principal
numero = int(input("Digite um número para o seu fatorial: "))
print(fatorial(numero, show=True))
help(fatorial)
