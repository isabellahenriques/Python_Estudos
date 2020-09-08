'''Faça um programa que tenha uma função notas()
que pode receber várias notas de alunos e vai retornar um dicionário
com as seguintes informações:
- Quantidade de notas
- A maior nota
- A menor nota
- A média da turma
- A situação (opcional)
Adicione também as docstrings dessa função para consulta pelo desenvolvedor.'''



def notas(*n, sit=False):
    """
    ->Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas do alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma.
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n)/len(n)
    if sit:
        if r['media'] >= 7:
            r['situação'] = 'BOA'
        elif r['media'] >= 5:
            r['situação'] = 'RAZOÁLVEL'
        else:
            r['situação'] = 'RUIM'
    return r


#Programa Principal
resposta = notas(5.5, 2.5, 2.5,sit=True)
print(resposta)
#help(notas)
