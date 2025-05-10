from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include, re_path
from django.views.static import serve

# Views that render the pages
from .views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index, name="index"),
    path("subscribe/", include("subscriptions.urls")),
    path("call/", include("calls.urls")),
    path("about", about, name="about"),
    path("contact", contact, name="contact"),
    path("services", services, name="services"),
    path("blog/", include(("blog.urls", "blog"), namespace="blog")),
    path("training/", include(("training.urls", "training"), namespace="training")),
    path("ckeditor/", include("ckeditor_uploader.urls")),
]

# This section is CRUCIAL for Render
if settings.DEBUG:
    # Serve media files during development (including on Render)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    # For production on Render
    urlpatterns += [
        re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    ]

# Additional security for production
if not settings.DEBUG:
    from django.views.defaults import page_not_found
    urlpatterns += [
        path('404/', page_not_found, {'exception': None}),
    ]