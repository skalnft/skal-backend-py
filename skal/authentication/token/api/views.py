from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.decorators import api_view
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status

from skal.cadastro.models import Usuario
from skal.utils.errors import InvalidWallet
from .serializers import CustomTokenObtainPairSerializer
from django.contrib.auth import authenticate
from django.http import Http404
from django.contrib.auth import get_user_model
from web3 import Web3


class CustomTokenObtainPairView(TokenObtainPairView):
    # Replace the serializer with your custom
    serializer_class = CustomTokenObtainPairSerializer

@api_view(http_method_names=['POST'])
def obtain_jwt_token(request):  # sourcery skip: raise-specific-error
    UserModel = get_user_model()

    try:
        wallet = request.data.get('wallet')
        username = request.data.get('username')
        # password = request.data.get('password')

        user = Usuario.objects.get(wallet=wallet, username=username)

        if not Web3.is_address(wallet):
            raise InvalidWallet(codigo_resposta=status.HTTP_401_UNAUTHORIZED, mensagem='Wallet do not exists')

        # user = authenticate(username=username, password=password)
        if not user:
            raise UserModel.DoesNotExist

        if user is None:
            return Response({'error': 'Credenciais inválidas'}, status=status.HTTP_401_UNAUTHORIZED)
        
        refresh = RefreshToken.for_user(user)
        
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'id': user.pk,
            'user': user.username,
        },
            status=status.HTTP_200_OK
        )
    except Exception as e:
        raise e