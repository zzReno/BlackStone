# Generated by Django 3.1.5 on 2021-01-25 21:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0015_containers_flag_string'),
    ]

    operations = [
        migrations.RenameField(
            model_name='topicname',
            old_name='flag_strings',
            new_name='flag_string',
        ),
    ]
