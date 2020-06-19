from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Recipe, Ingredient, Direction, Unit, Category


class RecipeForm(forms.ModelForm):

    class Meta:
        model = Recipe
        fields = [
            'name', 'ingredients', 'categories', 'time_needed', 'image_url',
            'recipe_ref', 'notes'
        ]
        exclude = ['user']
        widgets = {
            'ingredients': forms.CheckboxSelectMultiple(),
            'categories': forms.CheckboxSelectMultiple(),
            'notes': forms.Textarea(attrs={'rows': 5, 'cols': 50}),
        }

    def __init__(self, *args, **kwargs):
        #     self.user = kwargs.pop('user')
        #     super(RecipeForm, self).__init__(*args, **kwargs)
        super(RecipeForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
        self.fields['ingredients'].widget.attrs.update({
            'class': 'form-check-input',
            # 'class': 'form-inline'
        })
        self.fields['categories'].widget.attrs.update({
            'class': 'form-check-input'
        })


class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = [
            'name', 'amount', 'unit'
        ]

    def __init__(self, *args, **kwargs):
        super(IngredientForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })


class UnitForm(forms.ModelForm):
    class Meta:
        model = Unit
        fields = ['measure']

    def __init__(self, *args, **kwargs):
        super(UnitForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })


class DirectionForm(forms.ModelForm):
    class Meta:
        model = Direction
        fields = [
            'step', 'description', 'recipe'
        ]
        exclude = ('recipe',)

    def __init__(self, *args, **kwargs):
        super(DirectionForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

    def __init__(self, *args, **kwargs):
        super(CategoryForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })