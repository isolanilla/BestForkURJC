# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-29 10:25
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('prueba', '0005_historial'),
    ]

    operations = [
        migrations.AddField(
            model_name='historial',
            name='ref',
            field=models.CharField(default=datetime.datetime(2016, 3, 29, 10, 25, 27, 397009, tzinfo=utc), max_length=100),
            preserve_default=False,
        ),
    ]
