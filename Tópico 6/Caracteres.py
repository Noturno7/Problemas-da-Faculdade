frase = input ("Digite a sua frase: ")

while (len(frase) < 30 ):
    frase = input ("Sua frase tem menos de 30 caracteres! \nDigite novamente:")
else:
    print("Ok, sua frase tem mais de 30 caracteres!")

contadorDeLetras = 0
caracteres = input("Digite o caractere a ser computado: ")

for i in frase:
    if i == caracteres:
        contadorDeLetras += 1

print ("O caracter %s foi computado %d vezes na frase." %(caracteres, contadorDeLetras))