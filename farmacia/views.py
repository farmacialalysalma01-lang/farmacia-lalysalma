from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, "home.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/admin/")
        else:
            return render(request, "login.html", {"error": "Credenciais inválidas"})

    return render(request, "login.html")

from django.http import HttpResponse
from django.core.management import call_command

def run_migrate(request):
    if request.GET.get("key") != "farmacia2026":
        return HttpResponse("Acesso negado", status=403)

    call_comand("makemigrations","farmacia")
    call_command("migrate")
    return HttpResponse("Migrations executadas com sucesso!")
