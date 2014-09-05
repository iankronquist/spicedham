import os


ROOT = os.path.abspath(os.path.dirname(__file__))

SPICEDHAM = {
    'backend': 'DjangoOrmWrapper',
    'engine': 'sqlite:///./sqlite.db',
}

SECRET_KEY = 'super_secret'

DATABASES = {
    'default': {
        'NAME': ':memory:',
        'ENGINE': 'django.db.backends.sqlite3'
    }
}

INSTALLED_APPS = [
    #'elasticutils.contrib.django'
    
]
