# Generated by Django 4.1.7 on 2023-03-20 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_name', models.CharField(max_length=250)),
                ('p_decscription', models.TextField()),
                ('p_year', models.IntegerField()),
            ],
        ),
    ]
