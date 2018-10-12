# Generated by Django 2.1.2 on 2018-10-05 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avaliations', '0001_initial'),
        ('core', '0003_touristattraction_comentarios'),
    ]

    operations = [
        migrations.RenameField(
            model_name='touristattraction',
            old_name='comentarios',
            new_name='comments',
        ),
        migrations.AddField(
            model_name='touristattraction',
            name='avaliations',
            field=models.ManyToManyField(to='avaliations.Avaliation'),
        ),
    ]
