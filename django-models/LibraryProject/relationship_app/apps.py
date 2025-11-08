from django.apps import AppConfig


class RelationshipAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'relationship_app'

class RelationshipAppConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "relationship_app"

    def ready(self):
        # Import signals so receivers get registered at startup
        from . import signals  # noqa: F401