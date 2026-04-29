CAR = []

class CAR:
    def __init__(self, nome, modelo, ano, cor):
        self.nome = nome
        self.modelo = modelo
        self.ano = ano
        self.cor = cor

    def ligar(self):
        
        print(f"{self.nome} {self.modelo} está ligado.")