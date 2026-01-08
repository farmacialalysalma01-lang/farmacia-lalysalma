import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

application = get_wsgi_application()


# Auto migrate in Render
try:
    from django.core.management import call_command
    call_command("makemigrations", "farmacia")
    call_command("migrate")
except Exception as e:
    print("Migration error:", e)
