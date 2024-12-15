from django.apps import AppConfig


class BaseUserOverrideAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'base_user_override_app'
