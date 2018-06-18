# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from autoslug import AutoSlugField
from django.db import models
from ckeditor.fields import RichTextField

class Banner (models.Model):

    text = models.CharField(max_length=200)
    image = models.ImageField(upload_to='generic_pages_banner', null=True)

    class Meta:
		verbose_name_plural = 'Generic Banner'

    def __str__(self):

        return self.text

class Page(models.Model):
    publish_date = models.DateField()
    image = models.ImageField(upload_to='generic_pages_post', null=True, blank=True)
    publisher_name = models.CharField(max_length=200, blank=True)
    title = models.CharField(max_length=200)
    text = RichTextField(blank=True)
    author_first_name = models.CharField(max_length=200)
    author_last_name = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='title')
    publish = models.BooleanField(default=False)


    class Meta:
        verbose_name_plural = 'Generic Page'
    def __str__(self):
        return '''{}:'''.format(self.title)