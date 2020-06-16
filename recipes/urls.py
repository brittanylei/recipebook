from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:recipe_id>/', views.detail, name='detail'),
    path('addRecipe/', views.add_recipe, name='addrecipe'),
    path('<int:recipe_id>/deleteRecipe/', views.delete_recipe, name='delete'),
    path('<int:recipe_id>/editRecipe/', views.edit_recipe, name='edit'),
    path('addRecipe/addIngredient/', views.add_ingredient, name='addingredient'),
]