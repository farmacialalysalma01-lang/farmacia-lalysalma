from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("login/", views.login_view, name="login"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("recibo/<int:venda_id>/", views.recibo_pdf, name="recibo_pdf"),
]
