class Motor:
    def __init__(self, potencia: float, litragem: float, cilindros: int):
        self.potencia = potencia
        self.litragem = litragem
        self.cilindros = cilindros

    def __repr__(self):
        return f'{self.cilindros} |\n {self.litragem} |\n {self.potencia}'

class Carro:
    def __init__(self, motor: Motor, marca: str, nome: str):
        self.motor = motor
        self.marca = marca
        self.nome = nome


    def __repr__(self):
        return f'{self.motor} |\n {self.marca} |\n {self.nome}'


motor1 = Motor(245.00, 2.5, 4)

carro = Carro(motor1, 'ford', 'fusion')

