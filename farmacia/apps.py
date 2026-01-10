from django.apps import AppConfig

class FarmaciaConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "farmacia"

    def ready(self):
        from django.contrib.auth.models import User
        from django.db.utils import OperationalError

        try:
            if not User.objects.filter(username="admin").exists():
                User.objects.create_superuser(
                    username="admin",
                    password="Admin@2026",
                    email="admin@farmacialalysalma.com"
                )
        except OperationalError:
            pass
