from django.urls import path
from .views import (
    login_view,
    logout_view,
    area_caixa,
    nova_venda,
    adicionar_produto,
    finalizar_venda,
    historico_vendas,
    emitir_recibo
)

urlpatterns = [
    path("", login_view),
    path("login/", login_view),
    path("logout/", logout_view),

    path("caixa/", area_caixa),
    path("nova-venda/", nova_venda),
    path("adicionar-produto/", adicionar_produto),
    path("finalizar-venda/", finalizar_venda),

    path("historico-vendas/", historico_vendas),
    path("emitir-recibo/", emitir_recibo),
]
