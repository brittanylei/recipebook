
from django.core.mail.backends import console
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Recipe
from .forms import RecipeForm, IngredientForm, DirectionForm, UnitForm

# Create your views here.


def index(request):
    # return HttpResponse("Recipes")
    recipes = Recipe.objects.all()
    context = {'recipes': recipes}
    return render(request, 'index.html', context)


def detail(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    context = {'recipe': recipe}
    return render(request, 'detail.html', context)


def add_recipe(request):
    print("test")
    form = RecipeForm(request.POST or None)
    if form.is_valid():
        form.save()

    context = {'form': form}

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
    context = {'recipe': recipe}
    return render(request, 'editRecipe.html', context)