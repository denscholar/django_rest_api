# Generated by Django 4.1.7 on 2023-03-08 15:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog_app", "0004_category_rename_name_blog_blog_title_blog_category"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="blog",
            name="author",
        ),
    ]
