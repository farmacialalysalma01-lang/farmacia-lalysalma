from django.http import HttpResponse
from django.core.management import call_command
from django.contrib.auth.models import User

def setup_system(request):
    # rodar migrations
    call_command("makemigrations")
    call_command("migrate")

    # criar admin se não existir
    if not User.objects.filter(username="admin").exists():
        User.objects.create_superuser(
            username="admin",
            email="admin@farmacia.com",
            password="admin123"
        )

    return HttpResponse("Sistema configurado com sucesso!")
