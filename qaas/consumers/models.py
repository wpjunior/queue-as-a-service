from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse
from qaas.services.models import Service

class Consumer(models.Model):
    name = models.CharField(max_length=70)
    service = models.ForeignKey(
        Service,
        on_delete=models.PROTECT,
    )
    def get_absolute_url(self):
        return reverse('consumer-update', kwargs={'pk': self.pk})

