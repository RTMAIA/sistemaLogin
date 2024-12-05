from models.base import session
from models.cadastro_model import Cadastro


class Login:
    def logar(self, email, senha):
        x = session.query(Cadastro).filter_by(email=email).first()
        if x and x.verifica_hash(senha):
            return 'Login realizado!'
        else:
            return 'Senha incorreta!'
