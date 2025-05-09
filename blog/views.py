from django.shortcuts import render, get_object_or_404
from .models import *

from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post


class PostListView(ListView):
    model = Post
    template_name = "post_list.html"
    context_object_name = "posts"
    paginate_by = 6
    ordering = ["-created_on"]

    def get_queryset(self):
        return Post.objects.filter(status=1)  # Only published posts


class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = "post"
    slug_field = "slug"


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ["title", "main_image", "content", "category", "status"]
    template_name = "post_form.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ["title", "main_image", "content", "category", "status"]
    template_name = "post_form.html"
