# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from phonenumber_field.modelfields import PhoneNumberField

from django.db import models

class Banner (models.Model):

    text = models.CharField(max_length=200)
    image = models.ImageField(null=True)

    class Meta:
		verbose_name_plural = 'About Us Banner'

    def __str__(self):

        return self.text

class History_Section (models.Model):

    title = models.CharField(max_length=200)
    text = models.CharField(max_length=400)

    class Meta:
        verbose_name_plural = "History Section"

    def __str__(self):

        return self.title

class Director (models.Model):

    image = models.ImageField(null=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Directors'

    def __str__(self):

        return '{} {}: {}'.format(first_name, last_name, self.active)

class Staff_Member(models.Model):

    image = models.ImageField(null=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone = PhoneNumberField()
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Staff'

    def __str__(self):

        return '{} {}: {}'.format(first_name, last_name, self.active)

class Supporter_Section(models.Model):

    title = models.CharField(max_length=200)
    text = models.CharField(max_length=400)

    class Meta:
        verbose_name_plural = 'Supporter Section'

    def __str__(self):

        return self.title

class Supporter(models.Model):

    name = models.CharField(max_length=200)
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Supporters'

    def __str__(self):

        return '{}: {}'.format(self.name, self.active)
