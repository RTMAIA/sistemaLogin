from view.login_view import LoginView
from view.cadastrar_view import CadastrarView
from view.menu_view import MenuView

if __name__ == '__main__':
    while True:
        MenuView.menu()
        opc = int(input('>>'))
        if opc == 1:
            CadastrarView.cadastrar_view()
        if opc == 2:
            LoginView.login_view()