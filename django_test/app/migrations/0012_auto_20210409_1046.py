# Generated by Django 3.1.7 on 2021-04-09 00:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20210409_0851'),
    ]

    operations = [
        migrations.RenameField(
            model_name='people',
            old_name='eyeColor',
            new_name='eyecolor',
        ),
        migrations.RenameField(
            model_name='people',
            old_name='favoriteFoods',
            new_name='favoritefoods',
        ),
    ]
