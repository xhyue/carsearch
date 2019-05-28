# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-02-27 10:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carinfo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='carinfo',
            name='hprice',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=8, verbose_name='最高价格'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='carinfo',
            name='lprice',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=8, verbose_name='最低价格'),
            preserve_default=False,
        ),
    ]
