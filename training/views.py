from django.views.generic import ListView, DetailView
from .models import TrainingEvent

class TrainingListView(ListView):
    model = TrainingEvent
    template_name = "training/training_list.html"
    context_object_name = "events"
    ordering = ["start_datetime"]
    
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)

class TrainingDetailView(DetailView):
    model = TrainingEvent
    template_name = "training/training_detail.html"
    context_object_name = "event"