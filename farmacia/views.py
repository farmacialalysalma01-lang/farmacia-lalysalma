from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.db import connection
from django.contrib.auth.models import User
from django.core.management import call_command


# -------------- HOME ----------------
def home(request):
    return render(request, "home.html")


# -------------- LOGIN ----------------
def login_view(request):

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return HttpResponse("Login efectuado com sucesso!")
        else:
            return HttpResponse("Credenciais inválidas!")

    return render(request, "login.html")


# -------------- EXECUTAR MIGRATIONS ----------------
def run_migrate(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT 1")
        call_command("migrate")
    return HttpResponse("Migrações executadas com sucesso!")


# -------------- CRIAR ADMIN ----------------
def criar_admin(request):

    if User.objects.filter(username="admin").exists():
        return HttpResponse("O admin já existe!")

    User.objects.create_superuser(
        username="admin",
        password="admin123",
        email=""
    )

    return HttpResponse("Admin criado com sucesso!")
