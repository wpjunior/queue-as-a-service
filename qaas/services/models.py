from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse


class Service(models.Model):
    name = models.CharField(max_length=70)

    def get_absolute_url(self):
        return reverse('service-update', kwargs={'pk': self.pk})

    def __unicode__(self):
        return self.name
