# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-21 05:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='number_of_votes',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]