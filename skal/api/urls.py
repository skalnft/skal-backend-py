from django.urls import include, path

app_name = 'api'

urlpatterns = [
    path('', include('skal.evento.urls')),
    path('cadastro/', include('skal.cadastro.urls')),
]
