# Generated by Django 3.1 on 2020-09-02 05:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_auto_20200902_0800'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pickup',
            name='days',
        ),
    ]