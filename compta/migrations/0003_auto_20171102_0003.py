# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-01 23:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('compta', '0002_auto_20171101_2337'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=140)),
                ('somme', models.DecimalField(decimal_places=2, max_digits=11)),
                ('date', models.DateField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='budget',
            name='somme_actuelle',
            field=models.DecimalField(decimal_places=2, max_digits=11),
        ),
        migrations.AlterField(
            model_name='budget',
            name='somme_depart',
            field=models.DecimalField(decimal_places=2, max_digits=11),
        ),
        migrations.AddField(
            model_name='transaction',
            name='budget',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='compta.Budget'),
        ),
        migrations.AddField(
            model_name='transaction',
            name='compte',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='compta.Compte'),
        ),
    ]
