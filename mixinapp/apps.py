from django.apps import AppConfig


class MixinappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mixinapp'
