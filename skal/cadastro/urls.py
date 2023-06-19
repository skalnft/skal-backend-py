from django.urls import path, include
from rest_framework import routers
from skal.cadastro.usuario.api.views import UsuarioView

router = routers.DefaultRouter()
router.register(r'', UsuarioView, basename='cadastro')

urlpatterns = [
    path('', include(router.urls)),
]