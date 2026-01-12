from django.urls import path
from .views import login_view, logout_view, area_caixa, nova_venda, finalizar_venda

urlpatterns = [
    path("", login_view),
    path("login/", login_view),
    path("logout/", logout_view),
    path("caixa/", area_caixa),
    path("nova-venda/", nova_venda),
    path("finalizar-venda/", finalizar_venda),
]
