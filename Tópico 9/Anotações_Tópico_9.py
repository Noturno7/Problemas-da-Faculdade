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
