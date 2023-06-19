from rest_framework import viewsets
from skal.evento.ingresso.api.serializers import IngressoSerializer
from rest_framework.permissions import IsAuthenticated

from skal.evento.ingresso.models import Ingresso


class IngressoViewSet(viewsets.ModelViewSet):
    queryset = Ingresso.objects.all()
    serializer_class = IngressoSerializer
    permission_classes = [IsAuthenticated,]