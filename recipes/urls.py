from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:recipe_id>/', views.detail, name='detail'),
    path('addRecipe/', views.add_recipe, name='add-recipe'),
    path('<int:recipe_id>/deleteRecipe/', views.delete_recipe, name='delete-recipe'),
    path('<int:recipe_id>/editRecipe/', views.edit_recipe, name='edit-recipe'),
    path('addRecipe/addIngredient/', views.add_ingredient, name='add-ingredient'),
    path('<int:recipe_id>/editRecipe/addIngredient/', views.add_ingredient, name='edit-add-ingredient'),
    path('editRecipe/<int>:ingredient_id/deleteIngredient/', views.delete_ingredient, name='delete-ingredient'),
]