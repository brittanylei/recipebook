# Generated by Django 3.0.7 on 2020-07-17 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0029_auto_20200716_2354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='time_needed',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
