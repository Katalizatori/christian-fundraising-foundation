from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "author",
        "status",
        "created_on",
        "updated_on",
    )  # Fields to display in the list view
    list_filter = (
        "status",
        "created_on",
        "author",
    )  # Add filters for status, creation date, and author
    search_fields = (
        "title",
        "content",
    )  # Add a search bar to search by title or content
    prepopulated_fields = {
        "slug": ("title",)
    }  # Automatically populate the slug field based on the title
    raw_id_fields = ("author",)  # Use a dropdown or search widget for the author field
    date_hierarchy = "created_on"  # Add a date hierarchy navigation by creation date
    ordering = ("status", "-created_on")  # Default ordering for the list view
