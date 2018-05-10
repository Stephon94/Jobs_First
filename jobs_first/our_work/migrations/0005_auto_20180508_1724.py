# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-05-08 21:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('our_work', '0004_affiliates'),
    ]

    operations = [
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('sub_title', models.CharField(max_length=256, null=True)),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Sub_Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('image', models.ImageField(default='affiliates/No_person-1.jpg', upload_to='affiliates')),
                ('text', models.TextField()),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='our_work.Section')),
            ],
        ),
        migrations.RemoveField(
            model_name='affiliates',
            name='partner',
        ),
    ]
