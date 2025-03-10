from django.urls import path
from . import views

urlpatterns = [
    path('', views.resources, name="resources"),
    path('<int:post_id>/', views.article, name='post_detail'),
]