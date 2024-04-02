from django.apps import AppConfig


class CalledappConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "calledapp"
    
def ready(self):
        from .ap_scheduler import start
        start()
