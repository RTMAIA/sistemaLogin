from models.base import session
from models.cadastro_model import Cadastro


class AdicionarCadastroDAO:
    @classmethod
    def adicionar(cls, nome, email, senha):
        try:
            cls.cadastro = Cadastro(nome=nome, email=email)
            cls.cadastro.senha_hash(senha)
            session.add(cls.cadastro)
            session.commit()
            return 'Adicionado com sucesso!'
        except Exception as e:
            print(f'Ocorreu um erro: {e}')
            session.rollback()
