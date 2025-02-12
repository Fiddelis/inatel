# Faça um programa que leia o sexo de uma pessoa e diga se ela é
# homem (caso seja digitado M) ou mulher (caso seja digitado F). Caso
# seja digitado algo inválido, continue perguntando até que o usuário
# entre com um sexo válido

sexo = input("digite seu sexo (M/F): ")

while(sexo != "M" and sexo != "F"):
    sexo = input("digite seu sexo (M/F): ")

print("Masculino" if sexo == 'M' else "Feminino")