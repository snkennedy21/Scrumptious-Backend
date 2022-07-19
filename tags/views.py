from django.shortcuts import render
from recipes.models import Recipe
from django.views.generic import CreateView, UpdateView, DetailView
from django.urls import reverse_lazy

try:
    from tags.models import Tag
except Exception:
    Tag = None


# Create your views here.
def show_tags(request):
    context = {
        "tags": Tag.objects.all() if Tag else None,
    }
    return render(request, "tags/list.html", context)

class TagDetails(DetailView):
    model = Tag
    context_object_name = 'tag'
    template_name = 'tags/detail.html'

class CreateTag(CreateView):
    model = Tag
    template_name = 'tags/new.html'
    fields = ["name"]
    success_url = reverse_lazy('tags_list')

class EditTag(UpdateView):
    model = Tag
    template_name = 'tags/edit.html'
    fields = ["name"]
    success_url = reverse_lazy('tags_list')

def delete_tag(request):
    pass

