from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("", views.home, name="home"),
    path("login/", views.login_view, name="login"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("recibo/<int:venda_id>/", views.recibo_pdf, name="recibo_pdf"),
    path("logout/", LogoutView.as_view(next_page="/"), name="logout"),
]
