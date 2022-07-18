from django.urls import path
from recipes.views import ShowRecipesView, RecipeDetailView, CreateRecipe

from recipes.views import (
    change_recipe,
    ShowRecipesView,
    RecipeDetailView,
    CreateRecipe
)


urlpatterns = [
    path("", ShowRecipesView.as_view(), name="recipes_list"),
    path("<int:pk>/", RecipeDetailView.as_view(), name="recipe_detail"),
    path("new/", CreateRecipe.as_view(), name="recipe_new"),
    path("edit/", change_recipe, name="recipe_edit"),
]
