from rest_framework import viewsets
from skal.evento.models import Evento
from skal.evento.ingresso.models import Ingresso
from .serializers import EventoSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action


class EventoViewSet(viewsets.ModelViewSet):
    queryset = Evento.objects.pega_eventos_publicados()
    serializer_class = EventoSerializer
    # permission_classes = [IsAuthenticated,]

    @action(methods=['get'], detail=False, url_path='listar-eventos')
    def listar_eventos(self, request):
       return Response(EventoSerializer(self.queryset).data, many=True)


