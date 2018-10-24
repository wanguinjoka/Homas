# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-24 14:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='breakfast',
            name='week',
        ),
        migrations.RemoveField(
            model_name='clean',
            name='week',
        ),
        migrations.RemoveField(
            model_name='item',
            name='author',
        ),
        migrations.RemoveField(
            model_name='item',
            name='week',
        ),
        migrations.RemoveField(
            model_name='lunch',
            name='week',
        ),
        migrations.RemoveField(
            model_name='note',
            name='author',
        ),
        migrations.RemoveField(
            model_name='note',
            name='week',
        ),
        migrations.RemoveField(
            model_name='supper',
            name='week',
        ),
        migrations.RemoveField(
            model_name='week',
            name='image',
        ),
        migrations.DeleteModel(
            name='Breakfast',
        ),
        migrations.DeleteModel(
            name='Clean',
        ),
        migrations.DeleteModel(
            name='Item',
        ),
        migrations.DeleteModel(
            name='Lunch',
        ),
        migrations.DeleteModel(
            name='Note',
        ),
        migrations.DeleteModel(
            name='Supper',
        ),
    ]
