# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-05-21 19:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0001_initial'),
    ]

    operations = [
    migrations.RenameField('News', 'is_featured', 'is_news'),
    ]
