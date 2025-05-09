from django import forms
from .models import CallRequest


class CallRequestForm(forms.ModelForm):
    class Meta:
        model = CallRequest
        fields = "__all__"
