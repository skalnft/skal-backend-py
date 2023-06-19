from django.db import models


class EventoManager(models.Manager):
    def pega_eventos_publicados(self):
        return self.filter(esta_publico=True)