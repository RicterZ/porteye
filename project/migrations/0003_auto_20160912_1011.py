# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-09-12 02:11
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_auto_20160909_0937'),
    ]

    operations = [
        migrations.CreateModel(
            name='port_monitor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('ip_range', models.CharField(max_length=80)),
                ('check_frequency', models.IntegerField()),
                ('create_time', models.CharField(max_length=30)),
            ],
        ),
        migrations.AlterField(
            model_name='alertlog',
            name='insert_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 9, 12, 2, 11, 56, 520329)),
        ),
        migrations.AlterField(
            model_name='fnascanmetadata',
            name='insert_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2016, 9, 12, 10, 11, 56, 523186), null=True),
        ),
        migrations.AlterField(
            model_name='fnascanresult',
            name='update_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2016, 9, 12, 10, 11, 56, 521283), null=True),
        ),
        migrations.AlterField(
            model_name='masscanresult',
            name='update_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2016, 9, 12, 10, 11, 56, 522370), null=True),
        ),
    ]
