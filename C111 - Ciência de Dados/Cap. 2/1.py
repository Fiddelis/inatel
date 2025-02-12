# 1. Crie um programa que leia seu nome completo e mostre:
# • Seu nome com todas as letras maiúsculas
# • Seu nome com todas as letras minúsculas
# • Quantas letras ao todo tem seu nome
# • E como seria se trocássemos seu último nome para “do Inatel”

nome = str(input("Digite seu nome: "))

print("Nome com todas as letras maiúsculas:", nome.upper())
print("Nome com todas as letras minúsculas:", nome.lower())

nomes = nome.split(" ")
tamanho = sum(len(nome) for nome in nomes if len(nome))
print("Quantas letras ao todo tem seu nome:", tamanho)

nomes[len(nomes) - 1] = "do inatel"

nomes = " ".join(nomes)
print("Último nome trocado:", nomes)