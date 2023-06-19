from django.db import models


class AuthenticationManager(models.Manager):
    def recupera_usuario_por_wallet_username(self, wallet):
        self.filter(wallet=wallet).first()