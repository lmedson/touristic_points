# Generated by Django 2.1.4 on 2018-12-08 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_touristattraction_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='touristattraction',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='touristic_attractions'),
        ),
    ]
