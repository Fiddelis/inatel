# 5. Faça um programa que leia um número entre 1000 e 9999 e mostre na
# tela
# • qual o número da unidade
# • número da dezena
# • número da centena
# • E número do milhar

numero = float(input("Digite um numero entre 1000 e 9999: "))
while(numero < 1000 and numero > 9999):
    numero = float(input("Digite um numero entre 1000 e 9999: "))

unidade = numero % 10
dezena = (numero // 10) % 10
centena = (numero // 100) % 10
milhar = numero // 1000

print("Milhar: ", int(milhar))
print("Centena:", int(centena))
print("Dezena:", int(dezena))
print("Unidade:", int(unidade))