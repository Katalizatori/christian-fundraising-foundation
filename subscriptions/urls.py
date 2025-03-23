from django.contrib import admin
from django.urls import path, include

# Were the functions that render the pages are defined
from .views import *

urlpatterns = [
    path("", subscribe_view, name="subscribe"),
]
