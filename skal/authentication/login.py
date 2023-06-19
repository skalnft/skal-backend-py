from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

from skal.cadastro.models import Usuario


class MultiploLogin(ModelBackend):
    def authenticate(self, request, wallet=None, username=None, **kwargs):
        UserModel = get_user_model()
    #     try:
    #         manager = Usuario.objects
    #         user = manager.filter(wallet=wallet).first()

    #         if not user:
    #             raise UserModel.DoesNotExist
    #     except UserModel.DoesNotExist:
    #         return None
    #     else:
    #         if user.check_username(username):
    #             return user
    #     return None

    # def get_user(self, user_id):
    #     try:
    #         return Usuario.objects.get(pk=user_id)
    #     except Usuario.DoesNotExist:
    #         return None
