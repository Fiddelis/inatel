from motoristaDAO import MotoristaDAO
from motorista import Motorista
from passageiro import Passageiro
from corrida import Corrida

class MotoristaCLI:
    def __init__(self, motoristaDAO: MotoristaDAO):
        self.motoristaDAO = motoristaDAO

    def create_motorista(self):
        corridas = []

        while True:
            nota = int(input('Nota da corrida: '))
            distancia = float(input('Distância percorrida: '))
            valor = float(input('Valor da corrida: '))

            nome_passageiro = input('Nome do passageiro: ')
            documento_passageiro = input('Documento do passageiro: ')

            passageiro = Passageiro(nome_passageiro, documento_passageiro)
            corrida = Corrida(nota, distancia, valor, passageiro)

            corridas.append(corrida)

            if input('Deseja adicionar outra corrida? (S/N): ').strip().lower() != 's':
                break

        nota_media = sum(corrida.nota for corrida in corridas) // len(corridas)
        motorista = Motorista(corridas, nota)

        self.motoristaDAO.create_motorista(motorista)

    def read_motorista(self):
        motorista_id = input("ID do motorista: ")
        motorista = self.motoristaDAO.read_motorista_by_id(motorista_id)

        if motorista:
            print(f'Nota média: {motorista["nota"]}')
            print('Corridas: ')
            for corrida in motorista["corridas"]:
                passageiro = corrida["passageiro"]

                print(f'\tNota: {corrida["nota"]}')
                print(f'\tDistância: {corrida["distancia"]}')
                print(f'\tValor: {corrida["valor"]}')

                print('\tPassageiro: ')
                print(f'\t\tNome: {passageiro["nome"]}')
                print(f'\t\tDocumento: {passageiro["documento"]}')
        else:
            print("Motorista não encontrado.")

    def update_motorista(self):
        motorista_id = input("ID do motorista: ")
        motorista = self.motoristaDAO.read_motorista_by_id(motorista_id)

        if motorista:
            corridas = []

            while True:
                nota = int(input('Nota da corrida: '))
                distancia = float(input('Distância percorrida: '))
                valor = float(input('Valor da corrida: '))

                nome_passageiro = input('Nome do passageiro: ')
                documento_passageiro = input('Documento do passageiro: ')

                passageiro = Passageiro(nome_passageiro, documento_passageiro)
                corrida = Corrida(nota, distancia, valor, passageiro)

                corridas.append(corrida)

                if input('Deseja adicionar outra corrida? (S/N): ').strip().lower() != 's':
                    break

            nota_media = sum(corrida.nota for corrida in corridas) // len(corridas)
            novo_motorista = Motorista(corridas, nota_media)

            self.motoristaDAO.update_motorista_by_id(motorista_id, novo_motorista)
        else:
            print("Motorista não encontrado.")

    def delete_motorista(self):
        motorista_id = input("ID do motorista: ")
        self.motoristaDAO.delete_motorista(motorista_id)

    def run(self):
        print("Bem-vindo ao CLI do motorista!")
        print("Comandos disponíveis: create, read, update, delete, quit")

        while True:
            command = input("Digite um comando: ").strip().lower()

            if command == "quit":
                print("Até logo!")
                break
            elif command == "create":
                self.create_motorista()
            elif command == "read":
                self.read_motorista()
            elif command == "update":
                self.update_motorista()
            elif command == "delete":
                self.delete_motorista()
            else:
                print("Comando inválido. Tente novamente.")