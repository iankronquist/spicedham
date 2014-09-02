import json

from models import Store
from spicedham.basewrapper import BaseWrapper
from spicedham.config import load_config

class DjangoOrmWrapper(BaseWrapper):

    def __init__(self):
        """
        Create engine and session factory from config values.
        """
        config = load_config()

    def reset(self, really):
        """
        Delete all objects in the database if really is true.
        """
        if really:
            Store.objects.all().delete()

    def get_key(self, classifier, key, default=None):
        """
        Gets the value held by the classifier, key pair
        If it doesn't exist, return default.
        """
        store = Store.objects.filter(classifier=classifier, key=key).first()
        if store == None:
            value = default
        else:
            value = json.loads(store.value)
        return value

    def set_key(self, classifier, key, value):
        """
        Set the value held by the classifier, key pair
        """
        Store.objects.filter(classifier=classifier, key=key).update(value=value)
