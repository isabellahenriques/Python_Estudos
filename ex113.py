def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print("\033[31mErro: Digite um número inteiro válido!\033[m")
            continue
        except (KeyboardInterrupt):
            print("\033[31mUsuário preferiu não digitar esse número.\033[m")
            return 0
        else:
            return n


def leiaFLoat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print("\033[31mErro: Digite um número real válido!\033[m")
            continue
        except (KeyboardInterrupt):
            print("\033[31mUsuário preferiu não digitar esse número.\033[m")
            return 0
        else:
            return n


n1 = leiaInt("Digite um Inteiro: ")
n2 = leiaFLoat("Digite um Real: ")
print(f"O valor inteiro digitado foi {n1} e o real foi {n2}.")
