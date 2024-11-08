#Criando a Lista
Celsius = [-2.3, 0, 10, -15, -1, 3, 50, 22, -5.1, 33, 100, -100]

# Converter Celsius para Fahrenheit utilizando List Comprehension
Fahrenheit = [ ((float(9)/5)*temp + 32) for temp in Celsius ]

print(Fahrenheit)

# Ordenando e 'Melhorando' a visualização
Celsius.sort()
Fahrenheit.sort()
print("Graus Celsius\t\tGraus Fahrenheit")
print("------------------------------------------------------")
for i, j in zip(Celsius, Fahrenheit):
    print("%f\t\t%f" %(i, j))
    
#Perguntando ao usuário a partir de qual elemento(índice) ele deseja ver a lista
indice = int(input("A partir de qual elemento você deseja visualizar a lista? "))
print("Exibindo o resultado a partir do ",indice,"° elemento")
print("Graus Celsius\t\tGraus Fahrenheit")
print("------------------------------------------------------")
Celsius = Celsius[indice:]
Fahrenheit = Fahrenheit[indice:]
for i, j in zip(Celsius, Fahrenheit):
    print("%f\t\t%f" %(i, j))