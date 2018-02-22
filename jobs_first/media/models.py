# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ckeditor.fields import RichTextField

class News(models.Model):
    external_link = models.URLField(blank=True)
    publish_date = models.DateField()
    image = models.ImageField(null=True)
    publisher_name = models.CharField(max_length=200,blank=True)
    title = models.CharField(max_length=200)
    text = RichTextField(blank=True)
    author_first_name = models.CharField(max_length=200)
    author_last_name = models.CharField(max_length=200)
    slug = models.SlugField(blank=True)
    publish = models.BooleanField(default=False)
    is_news = models.BooleanField(default=False)


    class Meta:
        verbose_name_plural = 'News'
    def __str__(self):
        '''{}:
        {}
        {}'''.format(self.title, self.inPress, self.is_blogPost)
