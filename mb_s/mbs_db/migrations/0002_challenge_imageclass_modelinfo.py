# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-12-16 07:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mbs_db', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Challenge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='ImageClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('challenge', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mbs_db.Challenge')),
            ],
        ),
        migrations.CreateModel(
            name='ModelInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('train_challenge', models.CharField(max_length=30)),
                ('model_path', models.CharField(max_length=100)),
                ('label_dict', models.CharField(max_length=200)),
                ('challenge', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mbs_db.Challenge')),
            ],
        ),
    ]
