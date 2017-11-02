# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-01 22:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compta', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compte',
            name='somme_actuelle',
            field=models.DecimalField(decimal_places=2, max_digits=11),
        ),
        migrations.AlterField(
            model_name='compte',
            name='somme_depart',
            field=models.DecimalField(decimal_places=2, max_digits=11),
        ),
    ]
