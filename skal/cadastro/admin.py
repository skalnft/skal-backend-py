from django.contrib import admin
from skal.cadastro.models import Usuario


@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'wallet', 'username')
    search_fields = ('wallet', 'username', 'email')