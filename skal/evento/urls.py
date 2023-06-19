from django.urls import path, include

from rest_framework import routers
from skal.evento.api.views import EventoViewSet
from skal.evento.ingresso.api.views import IngressoViewSet

router = routers.DefaultRouter()
router.register(r'eventos', EventoViewSet)
router.register(r'ingressos', IngressoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]