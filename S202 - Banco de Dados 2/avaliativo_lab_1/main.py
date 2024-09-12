from motoristaCLI import MotoristaCLI
from motoristaDAO import MotoristaDAO
from database import Database

if __name__ == '__main__':
    motoristaDAO = MotoristaDAO('Inatel', 'Motorista')
    cli = MotoristaCLI(motoristaDAO)
    cli.run()