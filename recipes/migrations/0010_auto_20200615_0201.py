# Generated by Django 3.0.7 on 2020-06-15 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0009_auto_20200614_0644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]