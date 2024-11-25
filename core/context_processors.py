from .models import GlobalConfig

def global_config(request):
    config, created = GlobalConfig.objects.get_or_create(id=1)
    return {
        'allow_add_notes': config.allow_add_notes,
        'allow_view_evolution': config.allow_view_evolution,
    }
