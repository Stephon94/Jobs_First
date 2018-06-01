# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from autoslug import AutoSlugField
from django.db import models
from ckeditor.fields import RichTextField

class Banner (models.Model):

    text = models.CharField(max_length=200)
    image = models.ImageField(upload_to='news_banner',default= 'news_banner/no-banner-img.jpg')

    class Meta:
		verbose_name_plural = 'Media Banner'

    def __str__(self):

        return self.text

class News(models.Model):
    external_link = models.URLField(blank=True)
    publish_date = models.DateField()
    image = models.ImageField(upload_to='news_articles', null=True, blank=True)
    publisher_name = models.CharField(max_length=200, blank=True)
    title = models.CharField(max_length=200)
    text = RichTextField(blank=True)
    author_first_name = models.CharField(max_length=200)
    author_last_name = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='title')
    publish = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)


    class Meta:
        verbose_name_plural = 'News'
    def __str__(self):
        return '''{}:'''.format(self.title)