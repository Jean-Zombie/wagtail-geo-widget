# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-27 19:09
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geopage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='geopage',
            name='address',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='geopage',
            name='location',
            field=django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326),
        ),
    ]
