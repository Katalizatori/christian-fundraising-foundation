from django.shortcuts import render, get_object_or_404
from .models import *

# Create your views here.


def resources(request):
    """View function for the RESOURCES page of the site."""
    posts = Post.objects.filter(status=1)
    return render(request, "resources.html", {"posts": posts})


def article(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, "blog/post_detail.html", {"post": post})
