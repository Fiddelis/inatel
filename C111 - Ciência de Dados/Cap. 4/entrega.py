import numpy as np
from random import randint

# Exercício 1
# Criando arrays
arr1 = np.full(8, 1)  # Criando array de 1's
arr2 = np.random.randint(0, 10, size=8)  # Criando array de números aleatórios entre 0 e 9

print(arr1)
print(arr2)

# Somando arrays
arr_sum = np.add(arr1, arr2)
print(arr_sum)

# Transformando em matriz
if np.sum(arr_sum) >= 40:
    matrix = arr_sum.reshape(4, 2)
else:
    matrix = arr_sum.reshape(2, 4)

print(matrix)

# Exercício 2
# Criando arrays de números pares
array1 = np.arange(0, 52, 2)
array2 = np.arange(100, 48, -2)

print(array1)
print(array2)

# Concatenando e ordenando
array_concat = np.concatenate((array1, array2))
array_sorted = np.sort(array_concat)
print(array_sorted)

# Exercício 3 - Mini Campo Minado
campo = np.zeros((2, 2))
linha, coluna = np.random.randint(0, 2, size=2)
campo[linha, coluna] = 1
print(campo)

# Jogadas
tentativas = 3
acertou = False
for _ in range(tentativas):
    lin = int(input("Escolha a linha (0 ou 1): "))
    col = int(input("Escolha a coluna (0 ou 1): "))
    
    if campo[lin, col] == 1:
        print("Game Over! :(")
        acertou = True
        break
    else:
        print("Nenhuma bomba aqui!")

if not acertou:
    print("Parabéns! Você venceu o jogo!")

# Exercício 4
# Criando matriz
matriz = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
linhas, colunas = matriz.shape

# Verificando paridade
total_elementos = linhas * colunas
paridade = "par" if total_elementos % 2 == 0 else "ímpar"
print(f"A matriz pode ser transformada em um vetor com {paridade} número de elementos.")

# Exercício 5
np.random.seed(10)
matriz_random = np.random.randint(1, 51, (4, 4))
print(matriz_random)

# Cálculo das médias
media_colunas = matriz_random.mean(axis=0)
media_linhas = matriz_random.mean(axis=1)
print(f'Média das colunas: {media_colunas}')
print(f'Média das linhas: {media_linhas}')

# Maior média
max_media_linha = np.max(media_linhas)
max_media_coluna = np.max(media_colunas)
print(f'Maior média das linhas: {max_media_linha}')
print(f'Maior média das colunas: {max_media_coluna}')
