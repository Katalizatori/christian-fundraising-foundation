from django.db import models
from django.utils.timezone import now

class TrainingEvent(models.Model):
    event_id = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    url = models.URLField()
    image_url = models.URLField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['start_datetime']

    def __str__(self):
        return f"{self.name} ({self.start_datetime.date()})"