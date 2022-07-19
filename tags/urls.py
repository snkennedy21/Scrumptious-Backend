from django.urls import path

from tags.views import show_tags, CreateTag, TagDetails, EditTag

urlpatterns = [
    path("", show_tags, name="tags_list"),
    path("new/", CreateTag.as_view(), name="new_tag"),
    path("<int:pk>", TagDetails.as_view(), name="tag_detail"),
    path("<int:pk>edit/", EditTag.as_view(), name="tag_edit")
]
