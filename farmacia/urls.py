from django.urls import path
from . import views
from .views import run_migrate

urlpatterns = [
    path("", views.home, name="home"),
    path("login/", views.login_view, name="login"),
    path("run-migrate/", run_migrate, name="run_migrate"),
]
