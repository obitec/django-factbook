# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-22 16:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fact_book', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='continent',
            options={'verbose_name': 'Continent', 'verbose_name_plural': 'Continents'},
        ),
        migrations.AlterModelOptions(
            name='country',
            options={'ordering': ['display_name'], 'verbose_name': 'Country', 'verbose_name_plural': 'Countries'},
        ),
        migrations.AlterModelOptions(
            name='currency',
            options={'ordering': ['name'], 'verbose_name': 'Currency', 'verbose_name_plural': 'Currencies'},
        ),
        migrations.AlterModelOptions(
            name='region',
            options={'verbose_name': 'Region', 'verbose_name_plural': 'Regions'},
        ),
        migrations.AlterModelOptions(
            name='unitmeasure',
            options={'verbose_name': 'Measure', 'verbose_name_plural': 'Measures'},
        ),
        migrations.AlterField(
            model_name='continent',
            name='name',
            field=models.CharField(max_length=150, unique=True, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='country',
            name='name',
            field=models.CharField(max_length=150, unique=True, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='currency',
            name='code',
            field=models.CharField(max_length=3, unique=True, verbose_name='ISO code'),
        ),
        migrations.AlterField(
            model_name='currency',
            name='name',
            field=models.CharField(max_length=150, unique=True, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='currency',
            name='symbol',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Currency symbol'),
        ),
        migrations.AlterField(
            model_name='region',
            name='name',
            field=models.CharField(max_length=150, unique=True, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='unitmeasure',
            name='name',
            field=models.CharField(max_length=150, unique=True, verbose_name='Name'),
        ),
    ]
