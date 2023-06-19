from rest_framework import serializers
from skal.cadastro.models import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = 'id', 'wallet', 'username'
        # exclude = ('password',)