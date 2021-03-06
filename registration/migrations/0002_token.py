# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-26 13:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Token',
            fields=[
                ('username', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('token', models.CharField(max_length=64)),
                ('timestamp', models.IntegerField(default=0)),
                ('expiration', models.IntegerField(default=3600)),
            ],
        ),
    ]
