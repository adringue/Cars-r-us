# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-10-25 18:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0006_auto_20191024_1933'),
    ]

    operations = [
        migrations.AddField(
            model_name='lister',
            name='latitude',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='lister',
            name='longitude',
            field=models.FloatField(null=True),
        ),
    ]
