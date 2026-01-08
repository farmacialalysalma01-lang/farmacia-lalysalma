from django.http import HttpResponse, HttpResponseForbidden
from django.core.management import call_command
from django.contrib.auth.models import User

SETUP_KEY = "farmacia2026"  # 🔐 MUDE ESTA SENHA

def setup_system(request):
    key = request.GET.get("key")

    if key != SETUP_KEY:
        return HttpResponseForbidden("Acesso negado")

    # Executar migrations
    call_command("makemigrations")
    call_command("migrate")

    # Criar superuser se não existir
    if not User.objects.filter(username="admin").exists():
        User.objects.create_superuser(
            username="admin",
            email="admin@farmacia.com",
            password="admin123"
        )

    return HttpResponse("Sistema configurado com sucesso!")


    # criar admin se não existir
    if not User.objects.filter(username="admin").exists():
        User.objects.create_superuser(
            username="admin",
            email="admin@farmacia.com",
            password="admin123"
        )

    return HttpResponse("Sistema configurado com sucesso!")
