import random as rd # Contém funções para trabalhar aleatoriedade
import numpy as np #trabalhar com arrays

chances = '' #"Zerando" a variável
opcao = 'n' #Atribuindo valor "n"
minimo = '' #"Zerando" a variável
maximo = '' #"Zerando" a variável

#Boas Vindas ao "Desafiante"
print ("Vamos fazer uma disputa? Tente descobrir o número que estou pensando.")
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
        print()
    except:
        maximo = ''
        print("Digite um número inteiro válido, por favor!! \n")
        print()

#Usando placeholder para informar ao usuário o "range" de números que o computador pode escolher
print("Eu irei escolher um número entre %d e %d, OK?" %(minimo, maximo))

while opcao != 'S': #Aqui estamos controlando o valor digitado pelo usuário. Tem que ser inteiro válido
    
    exibir = np.arange(minimo, maximo + 1)
    num_aleatorio = rd.randrange(minimo, maximo + 1) #O valor máximo é exclusivo, por isso adicionamos 1
        
    cont = 1 #Contador para o número de tentativas
    
    print(exibir)
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
                    #Aqui estamos criando um array com os números que serão retirados da nossa lista para exibir ao usuário
                    faixa_ret = np.arange(min(exibir),num_tentativa + 1)
                    if len(exibir) > len(faixa_ret):
                        #A função setdiff1d retira do array "exibir" os objetos do array "faixa_ret"
                        #A condicional if é devido a função setdiff1d. Ela retira do array maior os objeos do array menor
                        exibir_novo = np.setdiff1d(exibir,faixa_ret) 
                    else:
                        exibir_novo = np.setdiff1d(faixa_ret,exibir) 
                    print ()

                elif num_tentativa > num_aleatorio and num_tentativa!='':
                    print ('o numero é mais baixo(-): ')
                    print ()
                    faixa_ret = np.arange(num_tentativa,max(exibir) + 1)
                    if len(exibir) > len(faixa_ret):
                        exibir_novo = np.setdiff1d(exibir,faixa_ret) 
                    else:
                        exibir_novo = np.setdiff1d(faixa_ret,exibir) 
                    print ()
                    
                print ('O número está entre estes: \n', exibir_novo, '\n')

                if num_tentativa!= '':
                    cont = cont + 1
                #Substituindo o array inicial "exibir" pelo array "exibir_novo" que é o resultado da diferença setdiff1d 
                exibir = exibir_novo
                
                num_tentativa = ''
                while num_tentativa == '':
                    try:
                        num_tentativa = input('tentativa %d: ' % cont)
                        print()
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