class InvalidWallet(ValueError):
    def __init__(self, codigo_resposta, mensagem):
        self.codigo_resposta = codigo_resposta
        self.mensagem = mensagem

    def __str__(self):
        return f'{self.codigo_resposta} - {self.mensagem}'
    
class UserAlreadyExists(ValueError):
    def __init__(self, codigo_resposta, mensagem):
        self.codigo_resposta = codigo_resposta
        self.mensagem = mensagem

    def __str__(self):
        return f'{self.codigo_resposta} - {self.mensagem}'