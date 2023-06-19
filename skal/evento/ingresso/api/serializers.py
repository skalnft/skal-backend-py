from rest_framework import serializers

from skal.evento.ingresso.models import Ingresso

class IngressoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingresso
        fields = '__all__'