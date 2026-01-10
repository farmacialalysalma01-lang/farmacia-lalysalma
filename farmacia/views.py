from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.management import call_command


def home(request):
    return render(request, "home.html")


def run_migrate(request):
    key = request.GET.get("key")

    if key != "farmacia2026":
        return HttpResponse("Acesso negado", status=403)

    call_command("migrate")

    return HttpResponse("Migração executada com sucesso")
