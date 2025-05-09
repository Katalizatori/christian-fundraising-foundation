from django.urls import path
from . import views

urlpatterns = [
    path(
        "", views.book_call, name="book_call"
    ),  # Empty path means it will load on /call/
    path("success/", views.success_page, name="success_page"),  # Success page
]
