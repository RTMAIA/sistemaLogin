from controller.login_controller import Login


class LoginView:
    @staticmethod
    def login_view():
        print('---------LOGIN--------')
        email = str(input('Digite email: '))
        senha = str(input('Digite senha: '))
        a = Login()
        print(a.logar(email, senha))
        exit()