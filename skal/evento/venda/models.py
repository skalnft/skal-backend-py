from django.db import models
from skal.evento.ingresso.models import Ingresso
from skal.evento.venda.manager.venda_manager import VendaManager
from django_currentuser.db.models import CurrentUserField


class Venda(models.Model):
    objects = VendaManager()
    ingresso = models.ForeignKey(Ingresso, on_delete=models.CASCADE)
    usuario = CurrentUserField()
    preco_total = models.FloatField()
    data_venda = models.DateTimeField()
    forma_pagamento = models.CharField(max_length=255, choices=())

    def __str__(self) -> str:
        return f'{self.ingresso}'
    