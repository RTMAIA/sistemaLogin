from DAO.adicionar_cadastro_DAO import AdicionarCadastroDAO


class CadastrarController:

    def cadastrar(self, nome, email, senha):
        try:
            if self.verifica_dados(nome, email, senha):
                AdicionarCadastroDAO.adicionar(nome, email, senha)
                return 'Cadastro realizado com sucesso!'
        except Exception as e:
         return f'Houve um erro: {e}'

    @classmethod
    def verifica_dados(cls, nome, email, senha):
        if not nome.isalpha:
            raise Exception('Este campo deve conter apenas letras!')
        if not '@' in email and not email.endswith('.com'):
            raise Exception('Esta campo deve conter um email valido!')
        if not len(senha)  >=8 and len(senha) <= 14:
            raise Exception('A senha deve conter o minimo de 8 digitos e maximo de 14!')
        if nome in senha:
            raise Exception('A senha nao pode conter seu nome!')
        if senha == int or senha.isdigit():
            if cls.verifica_sequencia_numerica(senha):
                raise Exception('A senha nao pode ser sequencia!')
        if senha == ord or senha.isalpha():
            if cls.verifica_sequencia_alpha(senha):
                raise Exception('A senha nao pode ser sequencia!')
        return True

    @classmethod
    def verifica_sequencia_numerica(cls, senha):
        return  all(int(senha[i]) == int(senha[i-1]) + 1 for i in range(1, len(senha)))

    @classmethod
    def verifica_sequencia_alpha(cls, senha):
        return  all(ord(senha[i]) == ord(senha[i-1]) + 1 for i in range(1, len(senha)))

