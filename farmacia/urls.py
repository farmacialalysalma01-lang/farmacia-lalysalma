from django.urls import path
from .views import login_view, logout_view, area_caixa

urlpatterns = [
    path("", login_view, name="login"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("caixa/", area_caixa, name="caixa"),
]
