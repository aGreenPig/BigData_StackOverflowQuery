from django.apps import AppConfig

class CodesearchConfig(AppConfig):
    name = 'codesearch'
    def ready(self):
        # Singleton utility
        # We load them here to avoid multiple instantiation across other
        # modules, that would take too much time.
        
        pass
     

