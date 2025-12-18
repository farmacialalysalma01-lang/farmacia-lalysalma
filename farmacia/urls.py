from django.urls import path
from .views import home, criar_admin

urlpatterns = [
    path("", home, name="home"),
    path("criar-admin/", criar_admin),
]
