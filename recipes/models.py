from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50)


class Recipe(models.Model):
    name = models.CharField(max_length=100)
    ingredients = models.ManyToManyField('Ingredient', related_name='ingredient_set')
    category = models.ManyToManyField('Category', related_name='category_set')
    time_needed = models.FloatField()
    image_url = models.CharField(max_length=255)
    recipe_ref = models.CharField(max_length=255, blank=True, default='')


class Unit(models.Model):
    measure = models.CharField(max_length=10, unique=True)


class Ingredient(models.Model):
    name = models.CharField(max_length=50)
    amount = models.FloatField()
    unit = models.ForeignKey('Unit', on_delete=models.CASCADE, blank=True, null=True)


class Direction(models.Model):
    step = models.IntegerField()
    description = models.CharField(max_length=100)
    recipe = models.ForeignKey('Recipe', on_delete=models.CASCADE, blank=True, null=True)