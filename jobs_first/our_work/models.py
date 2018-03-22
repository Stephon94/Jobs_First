# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from geopy.geocoders import Nominatim

geolocator = Nominatim()

class Banner (models.Model):

    text = models.CharField(max_length=200)
    image = models.ImageField(upload_to='our_work_banner',default= 'about_banner/no-banner-img.jpg')
    sub_image = models.ImageField(upload_to='our_work_banner', default='our_work_banner/solutions.jpg')

    class Meta:
		verbose_name_plural = 'Our Work Banner'

    def __str__(self):

        return self.text

class Partnership_Type (models.Model):

    title = models.CharField(max_length=200)
    text = models.CharField(max_length=400)

    class Meta:
        verbose_name_plural = "Type of Partnership"

    def __str__(self):

        return self.title

class Partner (models.Model):

    image = models.ImageField(upload_to='partner',default= 'partners/No_person-1.jpg')
    name = models.CharField(max_length=200)
    text = models.CharField(max_length=400)
    partnership_type = models.ForeignKey(Partnership_Type, on_delete=models.CASCADE, null=True)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=200)
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Partners'

    def get_coordinates(self):

        address = "{} {}, {}, {}".format(self.address, self.city, self.state, self.zipcode)
        return {(geolocator.geocode(address).latitude, geolocator.geocode(address).longitude):(self.name, self.text)}
    
    def __str__(self):

        return '{} :{}'.format(self.name, self.active)
