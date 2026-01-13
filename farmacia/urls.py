from django.urls import path
from . import views

urlpatterns = [
    path("", views.login_view, name="login"),
    path("login/", views.login_view),
    path("logout/", views.logout_view),

    path("caixa/", views.area_caixa),
    path("nova-venda/", views.nova_venda),
    path("finalizar-venda/", views.finalizar_venda),
    path("historico-vendas/", views.historico_vendas),
    path("emitir-recibo/", views.emitir_recibo),
]
