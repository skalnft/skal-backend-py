from django.db import models
from skal.cadastro.models import Usuario

from skal.evento.models import Evento


class Ingresso(models.Model):
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=True, blank=True)
    nft_token_id = models.CharField(max_length=255)
    preco = models.FloatField(null=True, blank=True)
    valido = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f'{self.evento}'
