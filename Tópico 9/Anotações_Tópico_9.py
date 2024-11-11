"""
situação_Escolar = dict()
aluno = list()
situação_Escolar['nome'] = str(input("Nome do aluno: "))
situação_Escolar['media'] = float(input("Média do aluno: "))

aluno.append(situação_Escolar)

for e in aluno:
    for k, v in e.items():
        print(f'O {k} é igual a {v}')
        
    # Condição de aprovação fora do loop que imprime os itens
    if e['media'] >= 7.5:
        print('O aluno está aprovado.')
    else:
        print('O aluno está reprovado.')
"""

import random
from time import sleep
from operator import itemgetter

jogoDados = dict()
partida = list()
ranking = list()

def jogarDados():
    return random.randrange(1,7)

jogoDados['jogador1'] = jogarDados()
jogoDados['jogador2'] = jogarDados()
jogoDados['jogador3'] = jogarDados()
jogoDados['jogador4'] = jogarDados()

partida.append(jogoDados)
resultado = jogarDados()
for e in partida:
    for k, v in e.items():
        print (f'O {k} tirou {v}')
        sleep(1)
print (f""""        
╔═══╗╔═══╗╔═══╗╔══╗╔╗─╔╗╔══╗─╔══╗───╔═══╗╔═══╗╔══╗╔╗╔╗╔╗──╔════╗╔══╗╔══╗─╔══╗
║╔══╝║╔══╝║╔═╗║║╔╗║║╚═╝║║╔╗╚╗║╔╗║───║╔═╗║║╔══╝║╔═╝║║║║║║──╚═╗╔═╝║╔╗║║╔╗╚╗║╔╗║
║║╔═╗║╚══╗║╚═╝║║╚╝║║╔╗─║║║╚╗║║║║║───║╚═╝║║╚══╗║╚═╗║║║║║║────║║──║╚╝║║║╚╗║║║║║
║║╚╗║║╔══╝║╔╗╔╝║╔╗║║║╚╗║║║─║║║║║║───║╔╗╔╝║╔══╝╚═╗║║║║║║║────║║──║╔╗║║║─║║║║║║
║╚═╝║║╚══╗║║║║─║║║║║║─║║║╚═╝║║╚╝║───║║║║─║╚══╗╔═╝║║╚╝║║╚═╗──║║──║║║║║╚═╝║║╚╝║
╚═══╝╚═══╝╚╝╚╝─╚╝╚╝╚╝─╚╝╚═══╝╚══╝───╚╝╚╝─╚═══╝╚══╝╚══╝╚══╝──╚╝──╚╝╚╝╚═══╝╚══╝
       """ )
sleep(2)

print (f""" 
╔═══╗╔═══╗╔══╗╔╗╔╗╔╗──╔════╗╔══╗╔══╗─╔══╗───╔══╗─╔══╗───╔═══╗╔══╗╔═══╗╔════╗╔══╗╔══╗─╔══╗
║╔═╗║║╔══╝║╔═╝║║║║║║──╚═╗╔═╝║╔╗║║╔╗╚╗║╔╗║───║╔╗╚╗║╔╗║───║╔═╗║║╔╗║║╔═╗║╚═╗╔═╝╚╗╔╝║╔╗╚╗║╔╗║
║╚═╝║║╚══╗║╚═╗║║║║║║────║║──║╚╝║║║╚╗║║║║║───║║╚╗║║╚╝║───║╚═╝║║╚╝║║╚═╝║──║║───║║─║║╚╗║║╚╝║
║╔╗╔╝║╔══╝╚═╗║║║║║║║────║║──║╔╗║║║─║║║║║║───║║─║║║╔╗║───║╔══╝║╔╗║║╔╗╔╝──║║───║║─║║─║║║╔╗║
║║║║─║╚══╗╔═╝║║╚╝║║╚═╗──║║──║║║║║╚═╝║║╚╝║───║╚═╝║║║║║───║║───║║║║║║║║───║║──╔╝╚╗║╚═╝║║║║║
╚╝╚╝─╚═══╝╚══╝╚══╝╚══╝──╚╝──╚╝╚╝╚═══╝╚══╝───╚═══╝╚╝╚╝───╚╝───╚╝╚╝╚╝╚╝───╚╝──╚══╝╚═══╝╚╝╚╝
""")
ranking = sorted(jogoDados.items(), key = itemgetter(1), reverse= True)
for i, v in enumerate(ranking):
    print(f'O {i+1}º colocado foi o {v[0]} com {v[1]}')
    sleep(1)

"""

Também é possível está resolução que utiliza mais os dicionários:

from random import randit
from time import sleep
from operator import itemgetter

jogo = {'jogador1'}: randint(1,6)
jogo = {'jogador2'}: randint(1,6)
jogo = {'jogador3'}: randint(1,6)
jogo = {'jogador4'}: randint(1,6)

ranking = dict()

print('Valores sorteados:')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)

ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('-=' *30)
print('== RANKING DOS JOGADORES ==')
for i, v in enumerate(ranking):
    print (f'{i+1}º lugar: {v[0]} com {v[1]}.')
    sleep(1)
    
"""