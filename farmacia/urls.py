from .views import executar_migracoes
from django.urls import path
from .views import home, criar_admin

urlpatterns = [
    path("", home, name="home"),
    path("criar-admin/", criar_admin),
    path("executar-migracoes/", executar_migracoes)
]
