from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Recipe, Ingredient, Direction, Unit


class RecipeForm(forms.ModelForm):

    class Meta:
        model = Recipe
        fields = [
            'name', 'ingredients', 'category', 'time_needed', 'image_url',
            'recipe_ref', 'notes'
        ]
        exclude = ['user']
        widgets = {
            'ingredients': forms.CheckboxSelectMultiple(),
            'category': forms.CheckboxSelectMultiple(),
            'notes': forms.Textarea(attrs={'rows': 5, 'cols': 50}),
        }

    # def __init__(self, *args, **kwargs):
    #     self.user = kwargs.pop('user')
    #     super(RecipeForm, self).__init__(*args, **kwargs)


class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = [
            'name', 'amount', 'unit'
        ]


class UnitForm(forms.ModelForm):
    class Meta:
        model = Unit
        fields = ['measure']


class DirectionForm(forms.ModelForm):
    class Meta:
        model = Direction
        fields = [
            'step', 'description', 'recipe'
        ]
        exclude = ('recipe',)

