
from django.core.mail.backends import console
from django.shortcuts import render
from django.http import HttpResponse
from .models import Recipe

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