from django.db import models


# http://stackoverflow.com/questions/3459843/auto-truncating-fields-at-max-length-in-django-charfields
class TruncatingCharField(models.CharField):
    def get_prep_value(self, value):
        value = super(TruncatingCharField, self).get_prep_value(value)
        if value:
            return value[:self.max_length]
        return value


class Store(models.Model):
    """
    A model representing a key value store.
    tag and key are composite primary keys (and thus unique as a pair).
    All columns are strings. Value is typically serialized json.
    Note that char fields truncate automatically.
    """
    key = TruncatingCharField(max_length=256)
    classifier = TruncatingCharField(max_length=256)
    value = TruncatingCharField(max_length=256)
    class Meta:
        unique_together = ("key", "classifier")
        app_label = 'asdf'

    def __unicode__(self):
        return unicode(classifier) + u' ' + unicode(key)
