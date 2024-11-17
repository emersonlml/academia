from django.apps import AppConfig


class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'
    verbose_name='Academia'
    
    
    #clss prof
class CoreConfig(AppConfig):
    name = 'core'
    
    def ready(self):
        import core.signals  # Importa el archivo signals para registrar las señales
