# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class News(models.Model):
    external_link = models.URLField()
    publish_date = models.DateField()
    image = models.
    title = models.CharField(max_length=200, blank=True)
    text = models.CharField(max_length=5000, blank=True) -- rich text field
    author_first_name = models.CharField(max_length=200)
    author_last_name = models.CharField(max_length=200)
    is_inPress = models.BooleanField(default=False)
    is_blogPost = models.BooleanField(default=False)


    class Meta:
        verbose_name_plural = 'News'
    def __str__(self):
        '''{}:
        {}
        {}'''.format(self.title, self.inPress, self.is_blogPost)
