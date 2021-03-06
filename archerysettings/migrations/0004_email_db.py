# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-03-11 06:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archerysettings', '0003_auto_20181209_0118'),
    ]

    operations = [
        migrations.CreateModel(
            name='email_db',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.TextField(blank=True, null=True)),
                ('message', models.TextField(blank=True, null=True)),
                ('recipient_list', models.EmailField(blank=True, max_length=254, null=True)),
            ],
        ),
    ]
