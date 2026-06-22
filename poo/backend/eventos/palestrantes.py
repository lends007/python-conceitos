class Palestrante:
    def __init__(self, nome: str, idade: int, curriculo: str, especialidade: str, custo: float):
        self.nome = nome
        self.idade = idade
        self.curriculo = curriculo
        self.especialidade = especialidade
        self.custo = custo

    def __repr__(self) -> str:
        return (
            f"{self.nome}\n"
            f"{self.idade}\n"
            f"{self.especialidade}\n"
            f"{self.custo}"
        )

