from django.contrib import admin
from django.urls import path, include

# Were the functions that render the pages are defined
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index, name="index"),
    path("about", views.about, name="about"),
    path("contact", views.contact, name="contact"),
    path("subscribe/", views.subscribe, name="subscribe"),
    path("success/", views.success, name="success"),
    path('blog/', include('blog.urls')), # DONE(3/3): Detail view for blogposts.
]
