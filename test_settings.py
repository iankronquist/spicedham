import os


ROOT = os.path.abspath(os.path.dirname(__file__))



SECRET_KEY = 'super_secret'

DATABASES = {
    'default': {
        'NAME': 'db.sqlite', 
        'ENGINE': 'django.db.backends.sqlite3'
    }
}

INSTALLED_APPS = [
#    'spicedham.contrib.django'
]
