from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'
    verbose_name = "Usuarios"

    def ready(self):
        from . import signals
