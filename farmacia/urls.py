from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("login/", views.login_view, name="login"),
    path("run-migrate/", views.run_migrate),   
    path("criar-admin/", views.criar_admin),   # 🚀 NOVA ROTA
]
