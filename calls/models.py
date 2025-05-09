from django.db import models

INCOME = (
    ("under_500k", "Less than £500K"),
    ("max_1m", "£500K - £1million"),
    ("max_3m", "£1 million - £3 million"),
    ("max_10m", "£3 million - £10 million"),
    ("over_10m", "Over £10 million"),
)


class CallRequest(models.Model):
    first_name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    organisation_name = models.CharField(max_length=200)
    role = models.CharField(max_length=100)
    annual_income = models.CharField(max_length=50, choices=INCOME)
    fundraisers = models.CharField(max_length=20)
    support_needs = models.TextField()
    privacy_policy = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.surname} from {self.organisation_name}"
