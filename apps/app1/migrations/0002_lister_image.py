# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-10-23 23:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lister',
            name='image',
            field=models.ImageField(null=True, upload_to='car_image'),
        ),
    ]
