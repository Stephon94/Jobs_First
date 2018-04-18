# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Banner (models.Model):

    text = models.CharField(max_length=200)
    image = models.ImageField(upload_to='home_banner',default= 'home_banner/no-banner-img.jpg')

    class Meta:
		verbose_name_plural = 'Home Page Banner'

    def __str__(self):

        return self.text

class Problem_Section(models.Model):

    title = models.CharField(max_length=200)
    text = models.TextField()

    class Meta:
		verbose_name_plural = 'Home Page Problem Section'

    def __str__(self):

        return self.title

class Solution_Section(models.Model):

    title = models.CharField(max_length=200)
    text = models.TextField()

    class Meta:
		verbose_name_plural = 'Home Page Solution Section'

    def __str__(self):

        return self.title

class Solution(models.Model):

    text = models.CharField(max_length=200)

    class Meta:
		verbose_name_plural = 'Home Page Solution Section: Solutions'

    def __str__(self):

        return self.text

class Impact_Section(models.Model):

    title = models.CharField(max_length=200)
    text = models.TextField()
    image = models.ImageField(upload_to='impact_banner',default= 'impact_banner/no-banner-img.jpg')

    class Meta:
		verbose_name_plural = 'Home Page Impact Section'

    def __str__(self):

        return self.title

class Impact_Section_Image(models.Model):

    image = models.ImageField(null=True)

    class Meta:
		verbose_name_plural = 'Impact Section Carousel Images'
