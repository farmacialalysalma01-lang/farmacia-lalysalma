from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, "home.html")

@login_required
def dashboard(request):
    return render(request, "dashboard.html")

from django.http import HttpResponse
from django.contrib.auth.models import User

def criar_admin(request):
    if User.objects.filter(username="admin").exists():
        return HttpResponse("Admin já existe")

    User.objects.create_superuser(
        username="admin",
        email="admin@farmacialalysalma.co.mz",
        password="Admin@2026"
    )
    return HttpResponse("Admin criado com sucesso")
