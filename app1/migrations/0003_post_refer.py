# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-10 08:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_auto_20180809_0850'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='refer',
            field=models.CharField(default=django.utils.timezone.now, max_length=500),
            preserve_default=False,
        ),
    ]