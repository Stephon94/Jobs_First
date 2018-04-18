# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-16 16:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about_us', '0005_auto_20180416_1119'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='director',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='director',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='staff_member',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='staff_member',
            name='last_name',
        ),
        migrations.AddField(
            model_name='director',
            name='name',
            field=models.CharField(default='John Doe', max_length=256),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='staff_member',
            name='name',
            field=models.CharField(default='John Doe', max_length=256),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='staff_member',
            name='text',
            field=models.TextField(default='John Doe'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='banner',
            name='text',
            field=models.CharField(max_length=256),
        ),
        migrations.AlterField(
            model_name='director',
            name='company',
            field=models.CharField(max_length=256),
        ),
        migrations.AlterField(
            model_name='director',
            name='position',
            field=models.CharField(max_length=256),
        ),
        migrations.AlterField(
            model_name='history_section',
            name='title',
            field=models.CharField(max_length=256),
        ),
        migrations.AlterField(
            model_name='staff_member',
            name='email',
            field=models.EmailField(max_length=256),
        ),
        migrations.AlterField(
            model_name='staff_member',
            name='position',
            field=models.CharField(max_length=256),
        ),
        migrations.AlterField(
            model_name='supporter',
            name='name',
            field=models.CharField(max_length=256),
        ),
    ]
