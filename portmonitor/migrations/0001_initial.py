# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-09-18 03:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ResultIp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taskid', models.IntegerField(blank=True, null=True)),
                ('inserted', models.DateTimeField(blank=True, null=True)),
                ('domain', models.CharField(blank=True, max_length=256, null=True)),
                ('address', models.CharField(blank=True, max_length=32, null=True)),
                ('is_up', models.IntegerField(blank=True, null=True)),
                ('os', models.CharField(blank=True, max_length=256, null=True)),
            ],
            options={
                'db_table': 'result_ip',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ResultPorts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taskid', models.IntegerField(blank=True, null=True)),
                ('inserted', models.DateTimeField(blank=True, null=True)),
                ('address', models.CharField(blank=True, max_length=256, null=True)),
                ('port', models.IntegerField(blank=True, null=True)),
                ('service', models.CharField(blank=True, max_length=256, null=True)),
                ('state', models.CharField(blank=True, max_length=12, null=True)),
                ('protocol', models.CharField(blank=True, max_length=12, null=True)),
                ('product', models.CharField(blank=True, max_length=64, null=True)),
                ('product_version', models.CharField(blank=True, max_length=64, null=True)),
                ('product_extrainfo', models.CharField(blank=True, max_length=128, null=True)),
                ('scripts_results', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'result_ports',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='FnascanMetadata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_id', models.IntegerField()),
                ('lastcheckts', models.IntegerField(default=0)),
                ('insert_time', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('portinfo', models.TextField(blank=True, default='', null=True)),
                ('port_data', models.TextField(blank=True, default='', null=True)),
                ('statistics', models.TextField(blank=True, default='', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='FnascanResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_id', models.IntegerField()),
                ('lastcheckts', models.DateTimeField(blank=True, null=True)),
                ('insert_time', models.DateTimeField(blank=True, null=True)),
                ('update_time', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('update_service_name_time', models.DateTimeField(blank=True, null=True)),
                ('update_web_title_time', models.DateTimeField(blank=True, null=True)),
                ('update_port_status_time', models.DateTimeField(blank=True, null=True)),
                ('ip', models.CharField(blank=True, max_length=18)),
                ('port', models.CharField(max_length=10)),
                ('service_name', models.TextField(blank=True, default='', null=True)),
                ('web_title', models.TextField(blank=True, default='', null=True)),
                ('service_detail', models.TextField(blank=True, default='', null=True)),
                ('port_status', models.BooleanField(default=True)),
                ('ip_status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='IpRemarks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taskid', models.IntegerField(blank=True, null=True)),
                ('inserted', models.DateTimeField(blank=True, null=True)),
                ('address', models.CharField(blank=True, max_length=32, null=True)),
                ('remarks', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='OpenPort',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_id', models.IntegerField()),
                ('lastcheckts', models.IntegerField(default=0)),
                ('insert_time', models.DateTimeField(blank=True, null=True)),
                ('update_time', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('update_banner_time', models.DateTimeField(blank=True, null=True)),
                ('ip', models.CharField(blank=True, max_length=18)),
                ('port', models.CharField(max_length=10)),
                ('banner', models.TextField(blank=True, default='', null=True)),
                ('port_status', models.BooleanField(default=True)),
                ('findby', models.CharField(default='', max_length=10)),
                ('updateby', models.CharField(default='', max_length=10)),
                ('remarks', models.TextField(blank=True, default='')),
            ],
        ),
        migrations.CreateModel(
            name='port_alive_project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('name', models.CharField(max_length=80)),
                ('port', models.IntegerField()),
                ('domain', models.CharField(max_length=80)),
                ('check_frequency', models.IntegerField()),
                ('notify_rule_id', models.IntegerField()),
                ('create_time', models.CharField(max_length=30)),
                ('status', models.IntegerField()),
                ('statusinfo', models.CharField(blank=True, max_length=512)),
                ('ports_check', models.BooleanField(default=False)),
                ('main_id', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='port_monitor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('ip_range', models.CharField(max_length=80)),
                ('check_frequency', models.IntegerField()),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('remarks', models.CharField(blank=True, max_length=512)),
                ('fnascan_check', models.BooleanField(default=False)),
                ('masscan_check', models.BooleanField(default=False)),
            ],
        ),
    ]