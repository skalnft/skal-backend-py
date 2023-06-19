from rest_framework import serializers

from skal.cadastro.usuario.api.serializers import UsuarioSerializer
from skal.evento.ingresso.api.serializers import IngressoSerializer
from skal.evento.models import Evento
from skal.evento.ingresso.models import Ingresso

class EventoSerializer(serializers.ModelSerializer):
    ingresso_set = serializers.SerializerMethodField()

    class Meta:
        model = Evento
        fields = '__all__'

    def get_ingresso_set(self, obj):
        ingressos = Ingresso.objects.filter(evento=obj)
        return IngressoSerializer(ingressos, many=True).data
