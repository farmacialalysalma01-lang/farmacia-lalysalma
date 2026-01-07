from django.core.management import call_command
from django.http import HttpResponse

def run_migrate(request):
    call_command("migrate")
    return HttpResponse("Migrações executadas com sucesso!")
path("run-migrate/", run_migrate),

