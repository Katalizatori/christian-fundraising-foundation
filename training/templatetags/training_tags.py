from django import template
from ..models import Training
from django.utils import timezone

register = template.Library()

@register.inclusion_tag("training/partials/_latest_trainings.html")
def show_latest_trainings(count=3):
    return {
        "latest_trainings": Training.objects.filter(is_active=True).order_by("-start_datetime")[:count]
    }

@register.inclusion_tag("training/partials/_upcoming_trainings.html")
def show_upcoming_trainings(count=3):
    return {
        "upcoming_trainings": Training.objects.filter(
            is_active=True,
            start_datetime__gte=timezone.now()
        ).order_by("start_datetime")[:count]
    }

@register.simple_tag
def upcoming_trainings_count():
    return Training.objects.filter(
        is_active=True,
        start_datetime__gte=timezone.now()
    ).count()