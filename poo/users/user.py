 from db import USERS

class User:
    def __init__(self, id, username, password, email):
        self.id = id
        self.username = username
        self.password = password
        self.email = email

    def add(self):
        USERS.append(self)    

    def __repr__(self):
        return f"{self.id}, \n username: {self.username}, \n user_email: {self.email} \n user_password: {self.password} \n is_admin: False"
    
    def update_username(self, username):
        user = User.get_user_by_id(self.id)
        if user:
            user.username = username
            return user
        return 'Usuário não encontrado'
    
    def update_password(self, password):
        user = User.get_user_by_id(self.id)
        if user:
            user.password = password
            return user
        return 'Usuário não encontrado'
    
    def update_email(self, email):
        user = User.get_user_by_id(self.id)
        if user:
            user.email = email
            return user
        return 'Usuário não encontrado'

class Cars:

    
    def __init__(self, marca, modelo, ano, cor):
        # Inicializa um objeto Carro com atributos básicos
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = (cor)
        self.ligado = False  # Status do carro (ligado/desligado)

    def ligar(self):
        # Método para ligar o carro
        if not self.ligado:
            self.ligado = True
            print(f"{self.marca} {self.modelo} está ligado.")
        else:
            print(f"{self.marca} {self.modelo} já está ligado.")

    def desligar(self):
        # Método para desligar o carro
        if self.ligado:
            self.ligado = False
            print(f"{self.marca} {self.modelo} está desligado.")
        else:
            print(f"{self.marca} {self.modelo} já está desligado.")

    def pintar(self, nova_cor): 
        self.cor = nova_cor
        nova_cor = {f"{self.cor}"}
        print(f"O carro agora é {self.cor}.")

    def exibir_informacoes(self):
        # Exibe todas as informações do carro
        status = "ligado" if self.ligado else "desligado"
        print(f"Carro: {self.marca} {self.modelo}, Ano: {self.ano}, Cor: {self.cor}, Status: {status}")


# Exemplo de uso
if __name__ == "__main__":
    carro1 = Cars("Fiat", "Marea", 2024, "preto enferrujado")
    carro1.exibir_informacoes()
    carro1.ligar()
    carro1.pintar("Sem cor")
    print("O Fiat Marea esta pegando fogo")
    carro1.exibir_informacoes()

    carro2 = Cars("Nissan", "R34", 2026, "Bryan(Velozes e Furiosos)")
    carro2.exibir_informacoes()
    carro2.ligar()
    carro2.pintar("Preto fosco")
    carro2.desligar()
    carro2.exibir_informacoes() 
