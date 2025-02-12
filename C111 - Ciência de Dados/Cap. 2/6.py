# 6. Peça ao usuário para entrar com um número decimal. Em seguida,
# aplique e mostre o resultado:
# • da raiz quadrada deste número
# • função teto
# • função chão
# • sua parte inteira

import math

numero = float(input("Entre com um numero decimal: "))

print("Raiz quadrada:", math.sqrt(numero))
print("Função teto:", math.ceil(numero))
print("Função chão:", math.floor(numero))
print("Parte Inteira:", math.trunc(numero))
