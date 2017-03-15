# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-14 22:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('travel_wishlist', '0002_auto_20170223_1909'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='date_visited',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='place',
            name='place_notes',
            field=models.CharField(default='exit', max_length=500),
            preserve_default=False,
        ),
    ]
