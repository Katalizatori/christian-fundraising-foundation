from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

# Were the functions that render the pages are defined
from .views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index, name="index"),
    path("subscribe/", include("subscriptions.urls")),
    path('call/', include('calls.urls')), # Include subscriptions URLs
    path("about", about, name="about"),
    path("contact", contact, name="contact"),
    path("services", services, name="services"),  # Added url paths for all pages.
     path('blog/', include(('blog.urls', 'blog'), namespace='blog')),
    path('training/', include(('training.urls', 'training'), namespace='training')),
    path("ckeditor/", include("ckeditor_uploader.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


