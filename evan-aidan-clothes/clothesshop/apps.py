from django.apps import AppConfig

class ClothesshopConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "clothesshop"

    def ready(self):
        import clothes.signals  # noqa