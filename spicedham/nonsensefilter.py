import operator
from itertools import imap, repeat

from spicedham.config import load_config
from spicedham.baseplugin import BasePlugin

class NonsenseFilter(BasePlugin):
    """
    Filter messages with no words in the database.
    """

    def __init__(self, config, backend):
        """
        Get values from the config.
        """
        self.backend = backend
        nonsensefilter_config = config.get('nonsensefilter', {})
        self.filter_match = nonsensefilter_config.get('filter_match', 1)
        self.filter_miss = nonsensefilter_config.get('filter_miss', None)
    
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
