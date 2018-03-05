# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-28 18:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('our_work', '0002_auto_20180221_2206'),
    ]

    operations = [
        migrations.AddField(
            model_name='banner',
            name='sub_image',
            field=models.ImageField(default='our_work_banner/solutions.jpg', upload_to='our_work_banner'),
        ),
        migrations.AlterField(
            model_name='banner',
            name='image',
            field=models.ImageField(default='about_banner/no-banner-img.jpg', upload_to='our_work_banner'),
        ),
        migrations.AlterField(
            model_name='partner',
            name='image',
            field=models.ImageField(default='partners/No_person-1.jpg', upload_to='partner'),
        ),
    ]
