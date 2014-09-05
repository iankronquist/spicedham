from django.conf import settings
from spicedham.baseconfig import BaseConfig

class SpicyDjangoConfig(BaseConfig):
    def load_config(self):
        return settings.SPICEDHAM
