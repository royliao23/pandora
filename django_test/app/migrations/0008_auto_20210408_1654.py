# Generated by Django 3.1.7 on 2021-04-08 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20210408_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='people',
            name='address',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='people',
            name='email',
            field=models.EmailField(max_length=255),
        ),
        migrations.AlterField(
            model_name='people',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='people',
            name='phone',
            field=models.CharField(max_length=255),
        ),
    ]
