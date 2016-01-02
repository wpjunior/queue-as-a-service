from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.db import models
from django.template.defaultfilters import slugify
from qaas.services.models import Service


class Consumer(models.Model):
    queue = models.SlugField(unique=True, verbose_name="Queue")
    name = models.CharField(max_length=70)
    service = models.ForeignKey(
        Service,
        on_delete=models.PROTECT,
    )
    
    def get_absolute_url(self):
        return reverse('consumer-update', kwargs={'pk': self.pk})


    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.queue:
            self.queue = slugify(self.name)
            
        return super(Consumer, self).save(*args, **kwargs)
