# from django.http import HttpResponse
# from django.template import loader
from django.shortcuts import render, redirect
from django.conf import settings
from mailchimp3 import MailChimp
from blog.models import Post  # from blog app


def index(request):
    """View function for the HOME page of the site. Fetches the 3 most recent blog posts and sends them to the site."""
    # DONE(3/3): Add functionality for querying for blog posts and other dynamic content.
    latest_posts = Post.objects.all().order_by("-created_on")[:3]

    context = {
        "latest_posts": latest_posts,
    }
    return render(request, "index.html", context)


def services(request):
    """View function for the ABOUT page of the site."""
    return render(request, "services.html")


def training(request):
    """View function for the TRAINING page of the site."""
    return render(request, "training.html")


def about(request):
    """View function for the ABOUT page of the site."""
    return render(request, "about.html")


def contact(request):
    """View function for the CONTACT page of the site."""
    return render(request, "contact.html")


def call(request):
    """View function for the CALL page of the site."""
    return render(request, "book-call.html")
