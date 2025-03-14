from django.contrib import admin
from django.urls import path, include

# Were the functions that render the pages are defined
from .views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path('blog/', include('blog.urls')), # DONE(3/3): Detail view for blogposts.
    path('', include('subscriptions.urls')),  # Include subscriptions URLs
    path("", index, name="index"),

    path("about", about, name="about"),
    path("contact", contact, name="contact"),

    path('services', services, name="services"), # Added url paths for all pages.
    path('training', training, name="training"),
]
