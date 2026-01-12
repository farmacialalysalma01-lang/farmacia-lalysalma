from django.urls import path
from .views import (
    login_view,
    logout_view,
    area_caixa,
    nova_venda,
    finalizar_venda,
    historico_vendas,
    emitir_recibo
)

urlpatterns = [
    path("", login_view, name="login"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),

    path("caixa/", area_caixa, name="caixa"),
    path("nova-venda/", nova_venda, name="nova_venda"),
    path("finalizar-venda/", finalizar_venda, name="finalizar_venda"),
    path("historico-vendas/", historico_vendas, name="historico_vendas"),
    path("emitir-recibo/", emitir_recibo, name="emitir_recibo"),
]
