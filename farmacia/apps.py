from django.apps import AppConfig


class FarmaciaConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "farmacia"

    def ready(self):
        from django.contrib.auth.models import User

        username = "admin"
        password = "Admin@2026"
        email = "admin@farmacia.com"

        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(
                username=username,
                email=email,
                password=password
            )
