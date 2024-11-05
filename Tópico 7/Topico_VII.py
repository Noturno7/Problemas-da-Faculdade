# Usando Numpy para trabalhar com arrays e listas.

# Carregando o pacote numpy
import numpy as np

# criando os arrays
arr1 = np.array([1.1, 1.2, 1.3, 1.4, 1.5])
arr2 = np.arange(4)
condicional = np.array([True, False, True, True, False])

# imprimindo na tela os arrays
print('arr1 = ', arr1)
print('arr2 = ', arr2)
print('condicional = ', condicional)

# 'Melhorando' a visualização
for x, y, c in zip(arr1, arr2, condicional):
    print(x, y, c)
    
# Sugestão de execução
resposta = [(x if c else y) for x, y, c in zip(arr1, arr2, condicional)]
print (resposta)
