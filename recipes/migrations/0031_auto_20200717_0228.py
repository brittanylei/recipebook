# Generated by Django 3.0.7 on 2020-07-17 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0030_auto_20200717_0107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='unit',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterUniqueTogether(
            name='ingredient',
            unique_together=set(),
        ),
        migrations.DeleteModel(
            name='Unit',
        ),
    ]
