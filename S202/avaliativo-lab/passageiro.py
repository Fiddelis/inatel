class Passageiro:
    def __init__(self, nome: str, documento: str) -> None:
        self.nome = nome
        self.documento = documento

    def get_info(self) -> dict:
        return {
            "nome": self.nome,
            "documento": self.documento
        }