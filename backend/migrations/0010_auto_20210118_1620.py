# Generated by Django 3.1.5 on 2021-01-18 16:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0009_resolver'),
    ]

    operations = [
        migrations.RenameField(
            model_name='resolver',
            old_name='image_name',
            new_name='topic_name',
        ),
    ]
