# Generated by Django 3.0.7 on 2020-06-13 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0004_auto_20200613_0122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='category',
            field=models.ManyToManyField(to='recipes.Category', verbose_name='category_set'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='ingredients',
            field=models.ManyToManyField(to='recipes.Ingredient', verbose_name='ingredient_set'),
        ),
    ]
