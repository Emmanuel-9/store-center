# Generated by Django 3.1 on 2020-08-27 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_slot'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slot',
            name='mass_of_good',
            field=models.IntegerField(),
        ),
    ]