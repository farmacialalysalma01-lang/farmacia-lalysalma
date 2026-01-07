from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

# Auto-migrate on startup
try:
    from django.core.management import call_command
    call_command('migrate', interactive=False)
except Exception as e:
    print("Migration error:", e)
