# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-31 10:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prueba', '0007_historicorepo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='historicorepo',
            old_name='notappal',
            new_name='repo',
        ),
    ]
