from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify


class Service(models.Model):
    topic = models.SlugField(unique=True, verbose_name="Topic")
    name = models.CharField(max_length=70, unique=True)
    description = models.TextField()

    def get_absolute_url(self):
        return reverse('service-update', kwargs={'pk': self.pk})

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.topic:
            self.topic = slugify(self.name)
            
        return super(Service, self).save(*args, **kwargs)
