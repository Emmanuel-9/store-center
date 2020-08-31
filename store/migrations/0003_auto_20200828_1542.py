# Generated by Django 3.1 on 2020-08-28 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20200828_1341'),
    ]

    operations = [
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('items', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='employee',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
    ]