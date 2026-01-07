from django.shortcuts import render

def home(request):
    return render(request, "home.html")

def login_view(request):
    return render(request, "login.html")

from django.http import HttpResponse
from django.core.management import call_command

def criar_admin(request):
    User.objects.create_superuser(
        username="admin",
        password="admin123",
        email=""
    )
    return HttpResponse("Admin criado com sucesso!")
