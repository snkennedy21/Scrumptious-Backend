from django.shortcuts import redirect, render

from django.views.generic import ListView

try:
    from recipes.forms import RecipeForm
    from recipes.models import Recipe
except Exception:
    RecipeForm = None
    Recipe = None


def create_recipe(request):
    if request.method == "POST" and RecipeForm:
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe = form.save()
            return redirect("recipe_detail", pk=recipe.pk)
    elif RecipeForm:
        form = RecipeForm()
    else:
        form = None
    context = {
        "form": form,
    }
    return render(request, "recipes/new.html", context)


def change_recipe(request, pk):
    if Recipe and RecipeForm:
        instance = Recipe.objects.get(pk=pk)
        if request.method == "POST":
            form = RecipeForm(request.POST, instance=instance)
            if form.is_valid():
                form.save()
                return redirect("recipe_detail", pk=pk)
        else:
            form = RecipeForm(instance=instance)
    else:
        form = None
    context = {
        "form": form,
    }
    return render(request, "recipes/edit.html", context)


def show_recipes(request):
    context = { 
        "recipes": Recipe.objects.all() if Recipe else [],
    }
    return render(request, "recipes/list.html", context)


class ShowRecipesView(ListView):
    model = Recipe
    context_object_name = 'recipes'
    template_name = 'recipes/list.html'


def show_recipe(request, pk):
    context = {
        "recipe": Recipe.objects.get(pk=pk) if Recipe else None,
    }
    return render(request, "recipes/detail.html", context)

