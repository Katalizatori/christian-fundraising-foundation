from django.db import models
from django.utils.timezone import now


class Training(models.Model):
    event_id = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    url = models.URLField()
    main_image = models.ImageField(
        upload_to="training/main_images/",
        blank=True,
        null=True,
        default="Summary",
        help_text="Featured image for cards and previews (Recommended: 1200x630px).",
    )
    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["start_datetime"]
        verbose_name_plural = "Trainings"

    def __str__(self):
        return f"{self.name} ({self.start_datetime.date()})"
