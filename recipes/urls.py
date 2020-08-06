from django.urls import path

from . import views

app_name = 'recipes'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:recipe_id>/', views.detail, name='detail'),
    path('addRecipe/', views.add_recipe, name='add-recipe'),
    path('<int:recipe_id>/deleteRecipe/', views.delete_recipe, name='delete-recipe'),
    path('<int:recipe_id>/editRecipe/', views.edit_recipe, name='edit-recipe'),
    path('addCategory/', views.add_category, name='add-category'),
    path('<category_name>/', views.index, name='category'),
]
