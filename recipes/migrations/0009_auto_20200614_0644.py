# Generated by Django 3.0.7 on 2020-06-14 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0008_auto_20200614_0634'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unit',
            name='measure',
            field=models.CharField(blank=True, max_length=10, unique=True),
        ),
    ]