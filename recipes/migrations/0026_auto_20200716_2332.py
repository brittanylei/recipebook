# Generated by Django 3.0.7 on 2020-07-16 23:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0025_auto_20200716_2330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='recipe',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='recipes.Recipe'),
        ),
    ]