# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-13 17:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cryptofolio', '0015_auto_20171213_1851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exchangebalance',
            name='currency',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='manualinput',
            name='currency',
            field=models.CharField(max_length=10),
        ),
    ]
