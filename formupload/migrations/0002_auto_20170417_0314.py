# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-17 03:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('formupload', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='grades',
            name='column4',
        ),
        migrations.RemoveField(
            model_name='grades',
            name='column5',
        ),
        migrations.RemoveField(
            model_name='grades',
            name='column6',
        ),
    ]
