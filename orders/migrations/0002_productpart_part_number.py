# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-04-07 10:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='productpart',
            name='part_number',
            field=models.CharField(default=0, max_length=8),
            preserve_default=False,
        ),
    ]
