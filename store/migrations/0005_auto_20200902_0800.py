# Generated by Django 3.1 on 2020-09-02 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_pickup_duration'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pickup',
            name='duration',
        ),
        migrations.AddField(
            model_name='pickup',
            name='days',
            field=models.IntegerField(null=True),
        ),
    ]