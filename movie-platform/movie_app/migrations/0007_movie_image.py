# Generated by Django 4.1.7 on 2023-03-20 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0006_alter_plant_s_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='image',
            field=models.ImageField(default=1, upload_to='images'),
            preserve_default=False,
        ),
    ]
