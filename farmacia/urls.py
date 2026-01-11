from django.urls import path
from . import views

urlpatterns = [
    path("", views.login_view, name="login"),
    path("caixa/", views.caixa, name="caixa"),
    path("farmaceutico/", views.farmaceutico, name="farmaceutico"),
    path("gerente/", views.gerente, name="gerente"),

    path("caixa/nova-venda/", views.nova_venda),
    path("caixa/historico/", views.historico_vendas),
    path("caixa/recibo/", views.emitir_recibo),
]
