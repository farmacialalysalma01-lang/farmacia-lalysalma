from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.core.management import call_command


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/admin/")
        else:
            return HttpResponse("Utilizador ou palavra-passe incorretos")

    return render(request, "login.html")


def run_migrate(request):
    if request.GET.get("key") != "farmacia2026":
        return HttpResponse("Acesso negado", status=403)

    call_command("makemigrations")
    call_command("migrate")

    return HttpResponse("Migrações executadas com sucesso")


def home(request):
    return HttpResponse("Sistema da Farmácia Lalysalma está ativo.")
