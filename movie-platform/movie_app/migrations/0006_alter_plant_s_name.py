# Generated by Django 4.1.7 on 2023-03-20 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0005_rename_p_year_plant_s_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plant',
            name='s_name',
            field=models.CharField(max_length=250),
        ),
    ]
