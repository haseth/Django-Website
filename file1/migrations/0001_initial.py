# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-07 18:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_text', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('list_text', models.CharField(max_length=200)),
                ('list_body', models.CharField(max_length=2000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ListReviews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reviews_text', models.CharField(max_length=200, null=True)),
                ('list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='file1.List')),
            ],
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subcategory_text', models.CharField(max_length=200)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='file1.Category')),
            ],
        ),
        migrations.AddField(
            model_name='list',
            name='subcategory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='file1.SubCategory'),
        ),
    ]