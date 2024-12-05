from os import system
from controller.cadastrar_controller import CadastrarController

class CadastrarView:
    @staticmethod
    def cadastrar_view():
        system('cls||clear')

        print('---------CADASTRAR----------')
        nome = str(input('Digite o nome: '))
        email = str(input('Digite o email: '))
        senha = str(input('Digite a senha: '))

        a = CadastrarController()
        print(a.cadastrar(nome, email, senha))