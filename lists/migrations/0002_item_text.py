# -*- coding: utf-8 -*-
# Generated by Django 2.0.5 on 2018-05-29 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("lists", "0001_initial")]

    operations = [
        migrations.AddField(
            model_name="item", name="text", field=models.TextField(default="")
        )
    ]
