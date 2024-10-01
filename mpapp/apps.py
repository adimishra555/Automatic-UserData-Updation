# from django.apps import AppConfig

# class MpappConfig(AppConfig):
#     default_auto_field = 'django.db.models.BigAutoField'
#     name = 'mpapp'

#     def ready(self):
#         # Import signals inside the ready method
#         from . import signals
       


from django.apps import AppConfig

class MpappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mpapp'

    def ready(self):
        import mpapp.signals 