from django.contrib import admin
from skal.evento.models import Evento
from skal.evento.ingresso.models import Ingresso
from skal.evento.venda.models import Venda


@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    ...

@admin.register(Ingresso)
class IngressoAdmin(admin.ModelAdmin):
    ...

@admin.register(Venda)
class VendaAdmin(admin.ModelAdmin):
    ...