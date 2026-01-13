from django.apps import AppConfig
from django.db import connection

class FarmaciaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'farmacia'

    def ready(self):
        try:
            with connection.cursor() as cursor:
                cursor.execute("""
                    DROP TABLE IF EXISTS farmacia_venda CASCADE;
                """)
        except:
            pass
