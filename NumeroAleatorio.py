import random # Contém funções para trabalhar aleatoriedade

chances = '' #"Zerando" a variável
opcao = 'n' #Atribuindo valor "n"
minimo = '' #"Zerando" a variável
maximo = '' #"Zerando" a variável

#Boas Vindas ao "Desafiante"
print ("Vamos fazer uma disputa? Tente descubrir o número que estou pensando.")
print ()
print ("""
Primeiro você irá escolher quantas tentativas você irá ter para descobrir meu número. \n
Depois você irá dizer quais são os limites mínimos e máximos para os números que eu posso escolher!! \n
Boa sorte!!
""")
print ()


while chances == '': #Aqui estamos controlando o valor digitado pelo usuário. Tem que ser inteiro válido

    """
    O try e except são tratamento de excessões. 
    A instrução try funciona da seguinte maneira:

    Primeiramente, a cláusula try (o conjunto de instruções entre as palavras reservadas try e except ) é executada.

    Se nenhuma exceção ocorrer, a cláusula except é ignorada e a execução da instrução try é finalizada.

    Se ocorrer uma execução durante a execução da cláusula try, as instruções remanescentes na cláusula são ignoradas. 

    Se o tipo da exceção ocorrida tiver sido previsto em algum except, então essa cláusula será executada. 

    Depois disso, a execução continua após a instrução try.

    A instrução try pode ter uma ou mais cláusula de exceção, para especificar múltiplos tratadores para diferentes exceções.
    """  
   
    try:
        chances = input("Digite a quantidade de chances que você quer para tentar me vencer: ")
        chances = int(chances)            
    except:
        chances = ''
        print("Digite um número inteiro válido, por favor!! \n")
    
while minimo == '': #Aqui estamos controlando o valor digitado pelo usuário. Tem que ser inteiro válido
    try:
        minimo = input("Digite o valor mínimo que eu posso escolher: ")
        minimo = int(minimo)            
    except:
        minimo = ''
        print("Digite um número inteiro válido, por favor!! \n")

while maximo == '': #Aqui estamos controlando o valor digitado pelo usuário. Tem que ser inteiro válido
    try:
        maximo = input("Digite o valor máximo que eu posso escolher: ")
        maximo = int(maximo)            
    except:
        maximo = ''
        print("Digite um número inteiro válido, por favor!! \n")

#Usando placeholder para informar ao usuário o "range" de números que o computador pode escolher
print("Eu irei escolher um número entre %d e %d, OK? \n" %(minimo, maximo))

while opcao != 'S': #Aqui estamos controlando o valor digitado pelo usuário. Tem que ser inteiro válido
    
    num_aleatorio = random.randrange(minimo, maximo + 1) #O valor máximo é exclusivo, por isso adicionamos 1
        
    cont = 1 #Contador para o número de tentativas
    
    print
    try:  
        num_tentativa = input('tentativa %d: ' % cont)
        num_tentativa = int(num_tentativa)
    except:
        num_tentativa = ''
        print ('Digite um número inteiro válido.')
            
    if num_tentativa!= '': #Após digitar um valor válido entramos nas condicionais para "descobrir o valor"
        while num_tentativa!= num_aleatorio and cont < chances:
                if num_tentativa == num_aleatorio:
                    break

                elif num_tentativa < num_aleatorio:
                    print ('o numero é mais alto(+): ')
                    print ()

                elif num_tentativa > num_aleatorio and num_tentativa!='':
                    print ('o numero é mais baixo(-): ')
                    print ()

                if num_tentativa!= '':
                    cont = cont + 1
                
                num_tentativa = ''
                while num_tentativa == '':
                    try:
                        num_tentativa = input('tentativa %d: ' % cont)
                        num_tentativa = int(num_tentativa)
                    except:
                        num_tentativa = ''
                        print ('Digite um número inteiro válido: ')
                        print ()

        if cont == chances and num_tentativa!= num_aleatorio:
            print ()
            print ('suas chances acabaram você perdeu!!!')
            print ('O número era', num_aleatorio)
            print ()

        else:
            print ()
            print ('Você acertou. Parabens!!!', num_tentativa)
            print ()
        #Permitindo ao usuário continuar no programa ou encerrar
        opcao = input('Para sair digite S. Para jogar novamente aperte qualquer tecla: ').upper()