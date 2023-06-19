from django.db import models


from django.db import models
from django.contrib.auth.models import AbstractUser

#from skal.cadastro.usuario.manager.usuario_manager import UsuarioManager


class Usuario(AbstractUser):
    # objects = UsuarioManager()
    wallet = models.CharField(max_length=255)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'

    def cria_novo_user(self, wallet, username, email=''):
        self.wallet = wallet
        self.username = username
        self.email = email
        
        return self

    def __str__(self) -> str:
        return self.wallet
    