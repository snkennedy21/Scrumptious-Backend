from django.urls import path
from recipes.views import ShowRecipesView, RecipeDetailView, CreateRecipe, UpdateRecipe, DeleteRecipe

from recipes.views import (
    UpdateRecipe,
    ShowRecipesView,
    RecipeDetailView,
    CreateRecipe,
    DeleteRecipe
)


urlpatterns = [
    path("", ShowRecipesView.as_view(), name="recipes_list"),
    path("<int:pk>/", RecipeDetailView.as_view(), name="recipe_detail"),
    path("new/", CreateRecipe.as_view(), name="recipe_new"),
    path("<int:pk>edit/", UpdateRecipe.as_view(), name="recipe_edit"),
    path("<int:pk>delete/", DeleteRecipe.as_view(), name="recipe_delete")
]
