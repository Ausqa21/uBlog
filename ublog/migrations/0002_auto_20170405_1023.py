# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-04-05 10:23
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ublog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 5, 10, 23, 53, 811064, tzinfo=utc)),
        ),
    ]
