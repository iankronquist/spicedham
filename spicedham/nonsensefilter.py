import operator
from itertools import imap, repeat

from spicedham.config import load_config
from spicedham.backend import load_backend
from spicedham.baseplugin import BasePlugin

class NonsenseFilter(BasePlugin):
    """
    Filter messages with no words in the database.
    """

    def __init__(self):
        """
        Get values from the config.
        """
        config = load_config()
        self.backend = load_backend()
        #self.filter_match = config['nonsensefilter']['filter_match']
        #self.filter_miss = config['nonsensefilter']['filter_miss']
        self.filter_match = 1
        self.filter_miss = 0
    
    def train(self, response, value):
        """
        Set each word to True.
        """
        self.backend.set_key_list(self.__class__.__name__, {(word, True) for word in response})

    # TODO: Will match responses consisting of only ''
    def classify(self, response):
        """
        If the message contains only words not found in the database return
        filter_match. Else return filter_miss.
        """
        classifier = self.__class__.__name__
        list_in_dict = lambda x, y: not self.backend.get_key(x, y, False)
        if all(imap(list_in_dict, repeat(classifier), response)):
            return self.filter_match
        else:
            return self.filter_miss
