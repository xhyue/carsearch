# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-02-27 09:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('carinfo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UnitImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caipiid', models.CharField(max_length=200, verbose_name='部件图片名称')),
                ('picture', models.ImageField(upload_to='img/car', verbose_name='图片')),
            ],
            options={
                'verbose_name': '部件图片',
                'db_table': 'unitimage',
                'verbose_name_plural': '部件图片',
            },
        ),
        migrations.CreateModel(
            name='UnitInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='标题')),
                ('desc', models.CharField(max_length=300, verbose_name='描述')),
                ('text', models.CharField(max_length=300, verbose_name='详情文字')),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carinfo.CarInfo')),
            ],
            options={
                'verbose_name': '部件表',
                'db_table': 'unitinfo',
                'verbose_name_plural': '部件表',
            },
        ),
        migrations.AddField(
            model_name='unitimage',
            name='unit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='unitinfo.UnitInfo'),
        ),
    ]