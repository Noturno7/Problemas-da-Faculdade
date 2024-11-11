entrevista = {}

candidatos = ["Gabriel F", "Fabin C", "Cleitin B"]

opcao = "n"

print ("Olá, estamos fazendo algumas entrevistas para saber o voto popular nesta eleição")
print()

while opcao != 'S' :
    idade = ''
    sexo = ''
    escolha = ''
    
    nome = input("Qual o seu nome?")
    print()
    
    while idade == '':
        try:
            idade = input("Qual a sua idade?")
            idade = int(idade)
        except:
            print("A idade deve ser um número valido!\n")
            idade = ''
    while sexo == '':
            sexo = input("""
Qual a opção que melhor te define?
M: Masculino.
F: Feminino.
O: outro não especificado anteriormente ou prefere não falar.

Escolha: """)
            if sexo in ("M","m","F","f","O","o"):
                sexo = sexo.upper()
                if sexo == "M":
                    sexo = "Masculino"
                elif sexo == "F":
                    sexo = "Feminino"
                elif sexo == "O":
                    sexo = "Outro"
                else:
                    sexo = ''
                    
            while escolha == '':
                escolha = input("""
Dos candidatos qual você ira votar?
1- Gabriel F
2- Fabin C
3- Cleitin B

Escolha: """)
                print()
                try:
                    escolha = int(escolha)
                except:
                    escolha = ''
                    print ()
                    print ("Digite um número valido!\n")
                    
                if escolha != '' and escolha not in range (1,4):
                    print()
                    print("Escolha uma das opções de voto valida por favor!")
                    
escolha = escolha - 1 # Atualização do índice

entrevista[nome] = [idade, sexo, candidatos[escolha]] # Criando o dicionário da pessoa entrevistada

# Resultado da votação individual
print('%s de %d anos, do sexo %s, votou em %s' %(nome, entrevista[nome[0]], entrevista[nome][1], entrevista[nome][2]))

# Exibindo o resultado da votação geral
print()
print("Situação da votação")
print('-=' *30)
print(f"{'Eleitor' : <40}|{'Idade' : ^7}| {'Sexo' : ^20}|{'Votou no Candito' : >20}")
print()
for nome, lista in entrevista.items():
    print(f'{nome: <40}|{lista[0] : ^7}|{lista[1] : ^20}|{lista[2] : >20}')
print()
opcao = input('Para encerrar a entrevista digite "S", ou aperte qualquer tecla para continuar: ').upper() 