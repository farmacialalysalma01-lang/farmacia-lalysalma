from django.urls import path
from .views import (
    login_view,
    logout_view,
    area_caixa,
    nova_venda,
    finalizar_venda,
)

urlpatterns = [
    path("", login_view, name="login"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),

    path("caixa/", area_caixa, name="caixa"),
    path("nova-venda/", nova_venda, name="nova_venda"),
    path("finalizar-venda/", finalizar_venda, name="finalizar_venda"),
]
