
from django.core.mail.backends import console
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Recipe, Ingredient, Direction, Category
from .forms import RecipeForm, IngredientForm, DirectionForm, UnitForm
from django.forms import modelformset_factory, formset_factory
from django.contrib import messages

# Create your views here.


def index(request, category_name=''):
    if category_name:
        recipes = Recipe.objects.filter(category__name=category_name)
    else:
        recipes = Recipe.objects.all()
    categories = Category.objects.all()
    context = {'recipes': recipes, 'categories': categories}
    return render(request, 'index.html', context)


def detail(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    context = {'recipe': recipe}
    return render(request, 'detail.html', context)


def add_recipe(request):
    form = RecipeForm(request.POST or None)
    d_set = modelformset_factory(model=Direction, form=DirectionForm, extra=3, exclude=())
    d_form = d_set(request.POST or None, request.FILES or None)
    recipe_name = request.POST.get('name',0)
    print(form.errors)
    print(form.non_field_errors())

    if form.is_valid():
        print("valid")
        form.save()
        recipe = Recipe.objects.get(name=recipe_name)
        if recipe and d_form.is_valid():
            for form in d_form:
                form = form.save(commit=False)
                form.recipe = recipe
                form.save()
            # d_form = d_form.save(commit=False)
            # d_form.recipe = recipe
            # d_form.save()
    context = {'form': form, 'd_form': d_form}
    return render(request, 'addRecipe.html', context)


def delete_recipe(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    if request.method == "POST":
        recipe.delete()
        return redirect("../../")
    context = {'recipe': recipe}
    return render(request, 'deleteRecipe.html', context)


def edit_recipe(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    form = RecipeForm(request.POST or None, instance=recipe)
    if form.is_valid():
        form.save()
        return redirect("../")
    context = {'recipe': recipe, 'form':  form}
    return render(request, 'editRecipe.html', context)


def edit_add_ingredient(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    form = IngredientForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("../")
    context = {'form': form, 'recipe': recipe}
    return render(request, 'addIngredient.html', context)


def add_ingredient(request):
    form = IngredientForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("../")
    context = {'form': form}
    return render(request, 'addIngredient.html', context)


def delete_ingredient(request, ingredient_id):
    ingredient = Ingredient.objects.get(id=ingredient_id)
    if request.method == "POST":
        ingredient.delete()
        return redirect("../../")
    context = {'ingredient': ingredient}
    return render(request, 'deleteIngredient.html', context)
