# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from autoslug import AutoSlugField
from django.db import models

class Banner (models.Model):

    text = models.CharField(max_length=200)
    image = models.ImageField(upload_to='publications_banner',default= 'publications_banner/no-banner-img.jpg')

    class Meta:
		verbose_name_plural = 'Publications Banner'

    def __str__(self):

        return self.text


class Article(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    is_featured = models.BooleanField(default=False)
    publish_date = models.DateField()
    author_first_name = models.CharField(max_length=200)
    author_last_name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='Article', blank=True ,null='True')
    pdf = models.FileField(upload_to='Article/pdf', blank=True ,null='True')
    slug = AutoSlugField(populate_from='title')

    class Meta:
        verbose_name_plural = 'Articles'
    def __str__(self):
        return '{} written by {} {}'.format(self.title, self.author_first_name, self.author_last_name)
