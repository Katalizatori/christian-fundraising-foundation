from django import template
from ..models import Post

register = template.Library()  # Must be named 'register'


@register.inclusion_tag("blog/partials/_latest_posts.html")
def show_latest_posts(count=3):
    return {
        "latest_posts": Post.objects.filter(status=1).order_by("-created_on")[:count]
    }
