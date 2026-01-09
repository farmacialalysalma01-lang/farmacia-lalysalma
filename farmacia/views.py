from django.http import HttpResponse
from django.shortcuts import render
from django.core.management import call_command


def run_migrate(request):
    if request.GET.get("key") != "farmacia2026":
        return HttpResponse("Acesso negado", status=403)

    call_command("makemigrations", "farmacia")
    call_command("migrate")

    return HttpResponse("Migrations executadas com sucesso!")


def home(request):
    return HttpResponse("Sistema da Farmácia Lalysalma está ativo.")
