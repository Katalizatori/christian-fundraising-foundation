from django.urls import path
from .views import *

app_name = "training"


urlpatterns = [
    path("", TrainingListView.as_view(), name="list"),
    path("all/", AllTrainingsView.as_view(), name="all"),
]