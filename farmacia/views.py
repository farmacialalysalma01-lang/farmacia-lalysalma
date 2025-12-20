from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def criar_admin(request):
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser(
            username='admin',
            email='admin@farmacialalysalma.co.mz',
            password='Admin@123'
        )
        return HttpResponse("Administrador criado com sucesso!")
    else:
        return HttpResponse("Administrador já existe.")
