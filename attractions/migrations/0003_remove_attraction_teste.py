# Generated by Django 2.1.2 on 2018-10-05 14:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attractions', '0002_attraction_teste'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attraction',
            name='teste',
        ),
    ]
