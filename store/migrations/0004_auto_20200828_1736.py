# Generated by Django 3.1 on 2020-08-28 14:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_auto_20200828_1542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slot',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='slots', to=settings.AUTH_USER_MODEL),
        ),
    ]
