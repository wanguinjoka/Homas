# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-24 14:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_supper'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clean',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room', models.CharField(max_length=100)),
                ('details', models.CharField(max_length=100)),
                ('week', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clean', to='home.Week')),
            ],
        ),
    ]
