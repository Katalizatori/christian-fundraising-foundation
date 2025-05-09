from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView

app_name = "blog"

urlpatterns = [
    path("", PostListView.as_view(), name="post_list"),
    path("<slug:slug>/", PostDetailView.as_view(), name="post_detail"),
    path("new/", PostCreateView.as_view(), name="post_create"),
    path("<slug:slug>/edit/", PostUpdateView.as_view(), name="post_update"),
]
