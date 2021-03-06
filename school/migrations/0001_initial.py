# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-03 14:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField(blank=True, max_length=52, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Schools',
                'verbose_name': 'School',
            },
        ),
    ]
