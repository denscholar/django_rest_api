# Generated by Django 4.1.7 on 2023-03-05 20:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog_app", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blog",
            name="created",
            field=models.DateField(default=datetime.date.today),
        ),
    ]
