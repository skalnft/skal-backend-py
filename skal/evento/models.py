from django.db import models
from skal.evento.manager.evento_manager import EventoManager

class Evento(models.Model):
    objects = EventoManager()
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    data = models.DateTimeField()
    localizacao = models.CharField(max_length=255)
    esta_publico = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.nome
