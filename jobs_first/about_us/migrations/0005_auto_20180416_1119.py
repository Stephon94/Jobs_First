# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-16 15:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about_us', '0004_auto_20180228_1851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history_section',
            name='text',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='supporter_section',
            name='text',
            field=models.TextField(),
        ),
    ]
