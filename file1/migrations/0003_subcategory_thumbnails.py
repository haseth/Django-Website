# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-17 22:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('file1', '0002_auto_20160608_0027'),
    ]

    operations = [
        migrations.AddField(
            model_name='subcategory',
            name='thumbnails',
            field=models.FileField(null=True, upload_to='documents/%Y/%m/%d'),
        ),
    ]