# Generated by Django 3.0.7 on 2020-07-15 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0019_auto_20200619_1852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='notes',
            field=models.TextField(blank=True, default='', max_length=1000),
        ),
    ]
