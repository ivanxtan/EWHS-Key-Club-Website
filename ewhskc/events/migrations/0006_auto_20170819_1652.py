# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-19 23:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_auto_20170819_1632'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='shift',
            options={'ordering': ['-time']},
        ),
    ]
