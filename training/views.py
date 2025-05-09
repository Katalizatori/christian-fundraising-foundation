from django.views.generic import ListView
from django.utils import timezone
from .models import Training

class AllTrainingsView(ListView):
    model = Training
    template_name = "training/all_trainings.html"
    context_object_name = "trainings"
    paginate_by = 12
    ordering = ["-created_on"]

    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)

    # Debug statement
    def get(self, request, *args, **kwargs):
        print("AllTrainingsView is being called!")
        return super().get(request, *args, **kwargs)
class TrainingListView(ListView):
    model = Training
    template_name = "training/list_trainings.html"
    context_object_name = "trainings"
    paginate_by = 12

    def get_queryset(self):
        queryset = super().get_queryset().filter(is_active=True)
        # Add any additional filtering logic here
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['upcoming_count'] = self.get_queryset().filter(
            start_datetime__gte=timezone.now()
        ).count()
        context['latest_count'] = self.get_queryset().count()
        return context


