from django.urls import path
from .views import criar_admin
from .views import home, criar_admin, executar_migracoes

urlpatterns = [
    path('', home, name='home'),
    path('criar-admin/', criar_admin),
    path('executar-migracoes/', executar_migracoes),

