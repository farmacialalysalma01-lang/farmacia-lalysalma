from django.urls import path
from . import views

urlpatterns = [
    path("", views.login_view, name="login"),
    path("home/", views.home, name="home"),
    path("caixa/", views.area_caixa, name="caixa"),
    path("caixa/nova-venda/", views.nova_venda, name="nova_venda"),
    path("logout/", views.sair, name="logout"),
]

