# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-04-07 12:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_productpart_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productpart',
            name='quantity',
            field=models.PositiveIntegerField(),
        ),
    ]
