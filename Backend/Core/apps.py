from django.apps import AppConfig


class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Core'
    
    #? Django Signal Configuration 
    def ready(self) :
        import Core.signals
    