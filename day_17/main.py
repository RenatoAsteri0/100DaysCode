class Car:

    # ATRIBUTO = oque TEM
    # funcao para registrar os ATRIBUTOS
    def __init__(self, id, username):       #__init__ = Inicialate, quando inicia a classe sempre é chamada essa funcao
        self.id = id
        self.username = username
        self.followers = 0
       #self = permite ATRIBUIR atributos idependente do usuario, no caso, user_1

    # METODO = oque FAZ
    def folow(self, user):
        user.followers += 1
        self.followers += 1

user_1 = Car('1', 'renato')
user_2 = Car('2', 'Bbeatriz')
print(user_1.username)