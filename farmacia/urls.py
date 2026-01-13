from django.urls import path
from . import views

urlpatterns = [
    path("", views.login_view, name="login"),
    path("caixa/", views.area_caixa, name="caixa"),
    path("nova-venda/", views.nova_venda, name="nova_venda"),
    path("finalizar-venda/", views.finalizar_venda, name="finalizar_venda"),
    path("historico-vendas/", views.historico_vendas, name="historico_vendas"),
    path("emitir-recibo/<int:venda_id>/", views.emitir_recibo, name="emitir_recibo"),
]
