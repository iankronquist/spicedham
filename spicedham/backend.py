from spicedham.config import load_config

#from elasticsearchwrapper import ElasticSearchWrapper


class BackendNotRecognizedException(Exception):
    """Possible backends are "sqlalchemy", "elasticsearch", and "djangoorm"""""
    pass

_backend = None

def load_backend():
    global _backend
    config = load_config()
    
    if _backend == None:
        # If this is a django config
        if config.__module__ == 'django.conf':
            from spicedham.contrib.spicedham import DjangoOrmWrapper
            _backend = DjangoOrmWrapper()
        elif  config['backend'] == 'sqlalchemy':
            from sqlalchemywrapper import SqlAlchemyWrapper
            _backend = SqlAlchemyWrapper()
        elif config['backend'] == 'elasticsearch':
            _backend = ElasticSearchWrapper()
        else:
            raise _backendNotRecognizedException
    return _backend
