from django.core.mail.backends import console
from django.shortcuts import render
from django.http import HttpResponse
from .models import Recipe

# Create your views here.


def index(request):
    # return HttpResponse("Recipes")
    recipes = Recipe.objects.all()
    return render(request, 'index.html', {'recipes': recipes})