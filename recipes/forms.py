from django import forms
from .models import Recipe, Ingredient, Category


class RecipeForm(forms.ModelForm):

    class Meta:
        model = Recipe
        fields = [
            'name', 'categories', 'time_needed', 'cover_img',
            'recipe_ref', 'notes'
        ]
        exclude = ['user']
        widgets = {
            'categories': forms.CheckboxSelectMultiple(),
            'notes': forms.Textarea(attrs={'rows': 5, 'cols': 50}),
        }

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super(RecipeForm, self).__init__(*args, **kwargs)

        for field in iter(self.fields):
            if field != 'categories':
                self.fields[field].widget.attrs.update({
                    'class': 'form-control'
                })


class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = [
            'recipe', 'name', 'amount', 'unit', 'prep'
        ]

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super(IngredientForm, self).__init__(*args, **kwargs)
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