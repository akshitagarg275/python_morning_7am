# Generated by Django 4.1.4 on 2022-12-12 02:01

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("youtubers", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="youtuber",
            name="description",
            field=ckeditor.fields.RichTextField(),
        ),
    ]
