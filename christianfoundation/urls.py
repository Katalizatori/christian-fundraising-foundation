from django.contrib import admin
from django.urls import path, include

# Were the functions that render the pages are defined
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('blog/', include('blog.urls')), # DONE(3/3): Detail view for blogposts.
    path("", views.index, name="index"),

    path("about", views.about, name="about"),
    path("contact", views.contact, name="contact"),

    path('services', views.services, name="services"), # Added url paths for all pages.
    path('training', views.training, name="training"),

    path("subscribe/", views.subscribe, name="subscribe"),
    path("success/", views.success, name="success"),
]
