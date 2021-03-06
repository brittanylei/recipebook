# Generated by Django 3.0.7 on 2020-06-13 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0005_auto_20200613_0523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='category',
            field=models.ManyToManyField(related_name='category_set', to='recipes.Category'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='ingredients',
            field=models.ManyToManyField(related_name='ingredient_set', to='recipes.Ingredient'),
        ),
    ]
