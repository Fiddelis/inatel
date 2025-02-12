# 4. Desenvolva um script que pergunte a distância de uma viagem em
# Km. Calcule o preço da passagem, cobrando R$0.50 por Km para viagens
# até 200Km e R$0.45 para viagens mais longas

distancia = float(input("Distância: "))
valor_cobrado = 0

if(distancia <= 200):
    valor_cobrado = 0.5
else:
    valor_cobrado = 0.45

print("Valor cobrado:", valor_cobrado)
print("Preço da passagem:", distancia * valor_cobrado)