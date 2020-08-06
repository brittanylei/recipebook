from django.shortcuts import render, redirect, get_object_or_404
from .models import Recipe, Ingredient, Category
from .forms import RecipeForm, CategoryForm
from django.forms import inlineformset_factory
from django.urls import reverse
from django.contrib.auth.decorators import login_required


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
    ingredFormSet = inlineformset_factory(Recipe, Ingredient, fields=('name', 'amount', 'unit', 'prep'), extra=10)
    form = RecipeForm(request.POST or None, request.FILES or None, request=request)
    formset = ingredFormSet(request.POST or None)

    if form.is_valid() and formset.is_valid():
        recipe = form.save(commit=False)
        recipe.user = request.user
        recipe.save()
        ingredients = formset.save(commit=False)

        for ingredient in ingredients:
            ingredient.recipe_id = recipe.id
            ingredient.save()

        form.save()
        return redirect(reverse('recipes:index'))

    context = {'form': form, 'formset': formset}
    return render(request, 'editRecipe.html', context)


@login_required(login_url='accounts:login')
def edit_recipe(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    ingredFormSet = inlineformset_factory(Recipe, Ingredient, fields=('name', 'amount', 'unit', 'prep'), extra=5)
    form = RecipeForm(request.POST or None, request.FILES or None, instance=recipe, request=request)
    formset = ingredFormSet(request.POST or None, instance=recipe)

    if form.is_valid() and formset.is_valid():
        form.save()
        formset.save()
        return redirect(reverse('recipes:detail', args=(recipe_id,)))

    context = {'recipe': recipe, 'form':  form, 'formset': formset}
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
def add_category(request):
    form = CategoryForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect("../")

    context = {'form': form}
    return render(request, 'addCategory.html', context)