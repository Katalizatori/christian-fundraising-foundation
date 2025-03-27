from django.urls import path
from .views import TrainingListView, TrainingDetailView

app_name = 'training'

urlpatterns = [
    path('', TrainingListView.as_view(), name='list'),
    path('<int:pk>/', TrainingDetailView.as_view(), name='detail'),
]