from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, "home.html")

from django.http import HttpResponse
from django.contrib.auth.models import User

def setup_admin(request):
    if User.objects.filter(username="admin").exists():
        return HttpResponse("Admin já existe")

    User.objects.create_superuser(
        username="admin",
        email="admin@farmacia.com",
        password="Admin@2026"
    )
    return HttpResponse("Admin criado com sucesso")

