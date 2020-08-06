from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User


class Category(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, unique=True)
    categories = models.ManyToManyField('Category', related_name='category_set', blank=True)
    time_needed = models.FloatField(blank=True, null=True)
    cover_img = models.ImageField(blank=True, null=True, upload_to="covers/")
    recipe_ref = models.CharField(max_length=255, blank=True, default='')
    notes = models.TextField(max_length=1000, default='', blank=True)

    def __str__(self):
        return self.name

    def get_cover(self):
        if not self.cover_img:
            return None
        else:
            return self.cover_img.url

    def get_icon(self):
        if self.cover_img:
            return self.cover_img.url
        else:
            return "/media/egg.jpg"


class Ingredient(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    amount = models.FloatField(validators=[MinValueValidator(0.0)])
    unit = models.CharField(max_length=20, null=True, blank=True)
    prep = models.CharField(max_length=25, default="", blank=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        if self.unit is None:
            return f'{str(self.amount)} {self.name}'

        return f'{str(self.amount)} {self.unit} {self.name} {self.prep}'


