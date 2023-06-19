from rest_framework import viewsets

from skal.cadastro.models import Usuario
from skal.cadastro.usuario.api.serializers import UsuarioSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

from skal.cadastro.usuario.use_cases.usuario_use_cases import UsuarioUseCase
from skal.utils.errors import UserAlreadyExists


class UsuarioView(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    http_method_names = ['get', 'post']

    @action(methods=['post'], detail=False, url_path='cria-novo-usuario')
    def cria_novo_usuario(self, request):
        try:
            wallet = request.data.get('wallet')
            username = request.data.get('username')
            # email = request.data.get('email')

            user = UsuarioUseCase().validar_usuario_para_criar(wallet, username)

            return Response(UsuarioSerializer(user).data, status=status.HTTP_201_CREATED)
        except UserAlreadyExists as e:
            raise UserAlreadyExists(
                mensagem='Wallet ou username já existe!', codigo_resposta=404
            ) from e
        except Exception as e:
            raise e
        
    def list(self, request, *args, **kwargs):
        return Response('Método não permitido', status=status.HTTP_403_FORBIDDEN)