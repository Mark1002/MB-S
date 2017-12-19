# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-12-16 13:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mbs_db', '0002_challenge_imageclass_modelinfo'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagefile',
            name='imageclass',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='mbs_db.ImageClass'),
            preserve_default=False,
        ),
    ]