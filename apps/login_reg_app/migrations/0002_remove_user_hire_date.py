# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-26 00:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login_reg_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='hire_date',
        ),
    ]
