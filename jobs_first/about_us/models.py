# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from phonenumber_field.modelfields import PhoneNumberField

from django.db import models

class Banner (models.Model):

    text = models.CharField(max_length=256)
    image = models.ImageField(upload_to='about_banner',default= 'about_banner/no-banner-img.jpg')

    class Meta:
		verbose_name_plural = 'About Us Banner'

    def __str__(self):

        return self.text

class History_Section (models.Model):

    title = models.CharField(max_length=256)
    text = models.TextField()

    class Meta:
        verbose_name_plural = "History Section"

    def __str__(self):

        return self.title

class Director (models.Model):

    image = models.ImageField(upload_to='directors',default= 'directors/No_person-1.jpg')
    name = models.CharField(max_length=256)
    position = models.CharField(max_length=256)
    company = models.CharField(max_length=256)
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Directors'

    def __str__(self):

        return '{}: {}'.format(self.name, self.active)

class Staff_Member(models.Model):

    image = models.ImageField(upload_to='staff',default= 'staff/No_person-1.jpg')
    name = models.CharField(max_length=256)
    position = models.CharField(max_length=256)
    text = models.TextField()
    email = models.EmailField(max_length=256)
    phone = PhoneNumberField()
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Staff'

    def __str__(self):

        return '{}: {}'.format(self.name, self.active)

class Supporter_Section(models.Model):

    title = models.CharField(max_length=200)
    text = models.TextField()

    class Meta:
        verbose_name_plural = 'Supporter Section'

    def __str__(self):

        return self.title

class Supporter(models.Model):

    name = models.CharField(max_length=256)
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Supporters'

    def __str__(self):

        return '{}: {}'.format(self.name, self.active)
