# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-26 06:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Authorization',
            fields=[
                ('username', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=32)),
            ],
        ),
    ]
