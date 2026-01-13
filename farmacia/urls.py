from django.urls import path
from .views import area_caixa, nova_venda, finalizar_venda, historico_vendas, emitir_recibo

urlpatterns = [
    path("caixa/", area_caixa),
    path("nova-venda/", nova_venda),
    path("finalizar-venda/", finalizar_venda),
    path("historico-vendas/", historico_vendas),
    path("emitir-recibo/", emitir_recibo),
]
