# 2. Mostre a tabuada de um número que o usuário escolher dentro de um
# intervalo específico também escolhido por ele

numero = int(input("Tabuado do numero: "))
intervalo1 = int(input("Valor do primeiro intervalo: "))
intervalo2 = int(input("Valor do segundo intervalo: "))

for i in range(intervalo1, intervalo2+1):
    print(numero, "x", i, "=", numero*i)

