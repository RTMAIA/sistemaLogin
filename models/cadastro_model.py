import bcrypt
from .base import Base
from sqlalchemy import  Column, Integer, String


class Cadastro(Base):
    __tablename__ = 'cadastro'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(50))
    email = Column(String(50), unique=True, nullable=False)
    senha = Column(String(128), nullable=False)

    def senha_hash(self, senha):
        self.senha = bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    def verifica_hash(self, senha):
        return bcrypt.checkpw(senha.encode('utf-8'), self.senha.encode('utf-8'))
