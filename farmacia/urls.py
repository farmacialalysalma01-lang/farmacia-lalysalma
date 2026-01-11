from django.urls import path
from . import views

urlpatterns = [
    path("", views.login_view, name="login"),
    path("caixa/", views.caixa, name="caixa"),
    path("farmaceutico/", views.farmaceutico, name="farmaceutico"),
    path("gerente/", views.gerente, name="gerente"),
]
