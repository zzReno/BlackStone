# Generated by Django 3.1.5 on 2021-01-26 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0017_resolver_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='topicname',
            name='score_type',
            field=models.BooleanField(default=True),
        ),
    ]