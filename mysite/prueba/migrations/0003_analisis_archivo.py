# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-23 11:02
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('prueba', '0002_auto_20160222_1724'),
    ]

    operations = [
        migrations.AddField(
            model_name='analisis',
            name='archivo',
            field=models.CharField(default=datetime.datetime(2016, 2, 23, 11, 2, 30, 397800, tzinfo=utc), max_length=100),
            preserve_default=False,
        ),
    ]