from django.shortcuts import render

def home(request):
    return render(request, "home.html")

def login_view(request):
    return render(request, "login.html")

from django.http import HttpResponse
from django.core.management import call_command

def run_migrate(request):
    call_command("migrate")
    return HttpResponse("Migrações executadas com sucesso!")
