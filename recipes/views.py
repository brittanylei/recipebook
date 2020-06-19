
from django.core.mail.backends import console
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Recipe, Ingredient, Direction, Category
from .forms import RecipeForm, IngredientForm, DirectionForm, UnitForm, CategoryForm
from django.forms import modelformset_factory, formset_factory
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required(login_url='accounts:login')
def index(request, category_name=''):
    if category_name:
        recipes = Recipe.objects.filter(categories__name=category_name, user=request.user)
    else:
        recipes = Recipe.objects.filter(user=request.user)
    categories = Category.objects.all()
    context = {'recipes': recipes, 'categories': categories}
    return render(request, 'index.html', context)


@login_required(login_url='accounts:login')
def detail(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    context = {'recipe': recipe}
    return render(request, 'detail.html', context)


@login_required(login_url='accounts:login')
def add_recipe(request):
    form = RecipeForm(request.POST or None)
    # d_set = modelformset_factory(model=Direction, form=DirectionForm, extra=3, exclude=())
    # d_form = d_set(request.POST or None, request.FILES or None)
    # recipe_name = request.POST.get('name',0)
    print(form.errors)
    print(form.non_field_errors())

    if form.is_valid():
        print("valid")
        recipe = form.save(commit=False)
        recipe.user = request.user
        recipe.save()
        form.save()
        # print(f'user: {form.cleaned_data["user"]}')
        # recipe = Recipe.objects.get(name=recipe_name)
        # if recipe and d_form.is_valid():
        #     for form in d_form:
        #         form = form.save(commit=False)
        #         form.recipe = recipe
        #         form.save()
        return redirect(reverse('recipes:index'))
    context = {'form': form}
    return render(request, 'editRecipe.html', context)


@login_required(login_url='accounts:login')
def delete_recipe(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    if request.method == "POST":
        recipe.delete()
        return redirect("../../")
    context = {'recipe': recipe}
    return render(request, 'deleteRecipe.html', context)


@login_required(login_url='accounts:login')
def edit_recipe(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    form = RecipeForm(request.POST or None, instance=recipe)
    if form.is_valid():
        form.save()
        return redirect("../")
    context = {'recipe': recipe, 'form':  form}
    return render(request, 'editRecipe.html', context)


@login_required(login_url='accounts:login')
def edit_add_ingredient(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    form = IngredientForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("../")
    context = {'form': form, 'recipe': recipe}
    return render(request, 'addIngredient.html', context)


@login_required(login_url='accounts:login')
def add_ingredient(request):
    form = IngredientForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("../")
    context = {'form': form}
    return render(request, 'addIngredient.html', context)


@login_required(login_url='accounts:login')
def delete_ingredient(request, ingredient_id):
    ingredient = Ingredient.objects.get(id=ingredient_id)
    if request.method == "POST":
        ingredient.delete()
        return redirect("../../")
    context = {'ingredient': ingredient}
    return render(request, 'deleteIngredient.html', context)


@login_required(login_url='accounts:login')
def add_category(request):
    form = CategoryForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("../")
    context = {'form': form}
    return render(request, 'addCategory.html', context)