from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    name = models.CharField(max_length=100, unique=True)
    ingredients = models.ManyToManyField('Ingredient', related_name='ingredient_set')
    category = models.ManyToManyField('Category', related_name='category_set', blank=True)
    time_needed = models.FloatField(blank=True)
    image_url = models.CharField(max_length=255, blank=True)
    recipe_ref = models.CharField(max_length=255, blank=True, default='')
    notes = models.CharField(max_length=1000, default='', blank=True)

    def __str__(self):
        return self.name


class Unit(models.Model):
    measure = models.CharField(max_length=10, unique=True, blank=True)

    def __str__(self):
        return self.measure


class Ingredient(models.Model):
    name = models.CharField(max_length=50)
    amount = models.FloatField()
    unit = models.ForeignKey('Unit', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        if self.unit is None:
            return f'{str(self.amount)} {self.name}'
        return f'{self.name} ({str(self.amount)} {self.unit.measure})'


class Direction(models.Model):
    step = models.IntegerField()
    description = models.CharField(max_length=100)
    recipe = models.ForeignKey('Recipe', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return str(self.step) + self.description
