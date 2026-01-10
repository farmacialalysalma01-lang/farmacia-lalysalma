from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.core.management import call_command


def home(request):
    return HttpResponse("Sistema da Farmácia Lalysalma está ativo.")


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/admin/")
        else:
            return HttpResponse("Credenciais inválidas")

    return HttpResponse("Página de login")


def run_migrate(request):
    key = request.GET.get("key")

    if key != "farmacia2026":
        return HttpResponse("Acesso negado", status=403)

    call_command("makemigrations")
    call_command("migrate")

    return HttpResponse("Migrações executadas com sucesso")
