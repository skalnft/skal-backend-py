from django.db.models import Q

from skal.cadastro.models import Usuario
from skal.utils.errors import UserAlreadyExists

class UsuarioUseCase:
    def execute(self):
        ...

    def validar_usuario_para_criar(self, wallet, username, email=''):
        try:
            # sourcery skip: raise-specific-error, use-named-expression
            usuario = Usuario.objects.filter(Q(
                Q(wallet=wallet) | Q(username=username)
            )).first()
            if usuario:
                raise UserAlreadyExists(mensagem='Wallet ou username já existe!', codigo_resposta=404)
            return Usuario().cria_novo_user(wallet, username, email)
        except Exception as e:
            raise e