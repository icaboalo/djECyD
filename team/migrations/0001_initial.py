# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-03 14:10
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bitacora',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assistance', models.BooleanField()),
                ('week_talk', models.BooleanField()),
                ('date', models.DateField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Bitacoras',
                'verbose_name': 'Bitacora',
            },
        ),
        migrations.CreateModel(
            name='Kid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=100)),
                ('slug', models.SlugField(blank=True, max_length=152, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Kids',
                'verbose_name': 'Kid',
            },
        ),
        migrations.CreateModel(
            name='Leader',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=100)),
                ('grade', models.CharField(choices=[('5 Primaria', '5 Primaria'), ('6 Primaria', '6 Primaria'), ('1 Secundaria', '1 Secundaria'), ('2 Secundaria', '2 Secundaria'), ('3 Secundaria', '3 Secundaria')], max_length=50)),
                ('slug', models.SlugField(blank=True, max_length=152, unique=True)),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.School')),
            ],
            options={
                'verbose_name_plural': 'Leaders',
                'verbose_name': 'Leader',
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('grade', models.CharField(choices=[('5 Primaria', '5 Primaria'), ('6 Primaria', '6 Primaria'), ('1 Secundaria', '1 Secundaria'), ('2 Secundaria', '2 Secundaria'), ('3 Secundaria', '3 Secundaria')], max_length=50)),
                ('slug', models.SlugField(blank=True, max_length=102, unique=True)),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teams', to='school.School')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teams', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Teams',
                'verbose_name': 'Team',
            },
        ),
        migrations.AddField(
            model_name='leader',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='team.Team'),
        ),
        migrations.AddField(
            model_name='kid',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='kids', to='team.Team'),
        ),
        migrations.AddField(
            model_name='bitacora',
            name='kid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bitacora', to='team.Kid'),
        ),
    ]
