# Generated by Django 3.2.1 on 2021-09-21 13:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogApp', '0002_alter_post_cat'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='cat',
            new_name='category',
        ),
    ]
