from django.http import HttpResponse
from django.contrib.auth.models import User

def criar_admin(request):
    if User.objects.filter(username='admin').exists():
        return HttpResponse("Admin já existe")

    User.objects.create_superuser(
        username='admin',
        email='admin@farmacialalysalma.co.mz',
        password='Admin@123'
    )
    return HttpResponse("Admin criado com sucesso")

