import os
import json

_config = None

def load_config():
    global _config
    try:
        import django
        os.environ['DJANGO_SETTINGS_MODULE'] = 'test_settings'
        from django.conf import settings
        _config = settings
    except ImportError:
        if _config == None:
            f = open('spicedham-config.json', 'r')
            _config = json.load(f)
    return _config
