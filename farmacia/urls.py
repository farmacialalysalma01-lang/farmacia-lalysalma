from django.urls import path
from . import views

urlpatterns = [
    path("", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),

    path("caixa/", views.caixa_dashboard, name="caixa"),
    path("caixa/nova-venda/", views.nova_venda, name="nova_venda"),
    path("caixa/historico/", views.historico_vendas, name="historico_vendas"),
    path("caixa/recibo/<int:venda_id>/", views.emitir_recibo, name="emitir_recibo"),
]

