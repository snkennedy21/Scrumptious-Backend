from django.contrib import admin
from .models import Recipe, Measure, FoodItem, Ingredient, Step, Tag

admin.site.register(Recipe)
admin.site.register(Measure)
admin.site.register(FoodItem)
admin.site.register(Ingredient)
admin.site.register(Step)
admin.site.register(Tag)
