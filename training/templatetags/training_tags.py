from django import template
from ..models import TrainingEvent

register = template.Library()

@register.inclusion_tag('training/partials/_latest_trainings.html')
def show_latest_trainings(count=3):
    return {
        'latest_trainings': TrainingEvent.objects.filter(
            is_active=True,
            start_datetime__gte=timezone.now()
        ).order_by('start_datetime')[:count]
    }