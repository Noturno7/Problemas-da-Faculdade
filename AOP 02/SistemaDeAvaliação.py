## Variáveis:
alunos = 100
aprovados = 0
reprovados = 0

## Loop para percorrer todos os alunos da faculdade:
for contador in range(1, alunos + 1):
    print(f"\nAluno: {contador}")
    
    ## Lógica utilizada para o recebimento e tratamento das notas dos alunos:
    while True:
        try:
            aop1 = float(input("Nota [0 - 1] na AOP1: Atividade Online Pontuada 1; "))
            if 0 <= aop1 <= 1:
                print("Nota [0 - 1] da AOP1 adicionada ao sistema.")
                break
            else:
                print("Valor inválido: A nota deve estar entre 0 e 1.")
        except:
            print("Valor inválido: Tente novamente um valor válido. O sistema lerá apenas NÚMEROS e PONTOS.")
    
    while True:
        try:
            aop2 = float(input("Nota [0 - 2] da AOP2: Atividade Online Pontuada 2; "))
            if 0 <= aop2 <= 2:
                print("Nota [0 - 2] da AOP2 adicionada ao sistema.")
                break
            else:
                print("Valor inválido: A nota deve estar entre 0 e 2.")
        except:
            print("Valor inválido: Tente novamente um valor válido. O sistema lerá apenas NÚMEROS e PONTOS.")
 
    while True:
        try:
            aop3 = float(input("Nota [0 - 1] na AOP3: Atividade Online Pontuada 3; "))
            if 0 <= aop3 <= 1:
                print("Nota [0 - 1] da AOP3 adicionada ao sistema.")
                break
            else:
                print("Valor inválido: A nota deve estar entre 0 e 1.")
        except:
            print("Valor inválido: Tente novamente um valor válido. O sistema lerá apenas NÚMEROS e PONTOS.")
            
    while True:
        try:
            provaPresecial = float(input("Nota [0 - 6] da PROVA REGULAR; "))
            if 0 <= provaPresecial <= 6:
                print("Nota [0 - 6] da PROVA REGULAR adicionada ao sistema.")
                break
            else:
                print("Valor inválido: A nota deve estar entre 0 e 6.")
        except:
            print("Valor inválido: Tente novamente um valor válido. O sistema lerá apenas NÚMEROS e PONTOS.")
    
    ## Fórmula para verificar se o aluno precisará de fazer a recuperação, já está reprovado ou passou direto:
    somaDoModulo = aop1 + aop2 + aop3 + provaPresecial
    
    if somaDoModulo < 3:
        print("Reprovado direto.")
        reprovados += 1
        continue
    
    ## Lógica para a implementação do recebimento da nota de recuperação do aluno:
    recuperacao = 0
    if somaDoModulo < 7:
        while True:
            try:
                recuperacao = float(input("Nota [0 - 10] da PROVA DE RECUPERAÇÃO: "))
                if 0 <= recuperacao <= 10:
                    print("Nota [0 - 10] da PROVA DE RECUPERAÇÃO adicionada ao sistema.")
                    break
                else:
                    print("Valor inválido: A nota deve estar entre 0 e 10.")
            except:
                print("Valor inválido: Tente novamente um valor válido. O sistema lerá apenas NÚMEROS e PONTOS.")

    ## Ajuste do cálculo da média para considerar a recuperação somente se ela for realizada:
    if somaDoModulo < 7:
        mediaDoModulo = (somaDoModulo + recuperacao) / 2
    else:
        mediaDoModulo = somaDoModulo

    if mediaDoModulo < 5:
        print("Reprovado após a prova de recuperação.")
        reprovados += 1
    else:
        print("Aprovado.")
        aprovados += 1

# Estatísticas finais:
total_alunos = aprovados + reprovados
porcentagem_aprovados = (aprovados / total_alunos) * 100
porcentagem_reprovados = (reprovados / total_alunos) * 100

print(f"\nEstatísticas finais:")
print(f"Percentual de alunos aprovados: {porcentagem_aprovados:.2f}%")
print(f"Percentual de alunos reprovados: {porcentagem_reprovados:.2f}%")


        
