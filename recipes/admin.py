from django.contrib import admin
from .models import Category, Recipe, Ingredient, Unit

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', )


class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name', )


class UnitAdmin(admin.ModelAdmin):
    list_display = ('measure', )


class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name', )


admin.site.register(Category, CategoryAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Unit, UnitAdmin)
admin.site.register(Ingredient, IngredientAdmin)
