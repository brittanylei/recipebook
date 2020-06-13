from django.contrib import admin
from .models import Category, Recipe, Ingredient, Direction, Unit

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', )

class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name', )


class UnitAdmin(admin.ModelAdmin):
    list_display = ('measure', )


class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name', )



class DirectionAdmin(admin.ModelAdmin):
    list_display = ('description', )


admin.site.register(Category, CategoryAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Unit, UnitAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Direction, DirectionAdmin)
