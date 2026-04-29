class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def apresenntar (self):
        print(f'Olá, meu nome é {self.username}.')


user1 = User('Kelwin', 'kelvindataisinha')
user2 = User('Maria', '548e343')

user1.apresenntar()
user2.apresenntar()