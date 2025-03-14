from django import forms



class BaseUserForm(forms.Form):
    name = forms.CharField(max_length=200, required=True, error_messages={'required': 'Please enter your name.'})
    surname = forms.CharField(max_length=200, required=True, error_messages={'required': 'Please enter your surname.'})
    email = forms.EmailField(required=True, error_messages={'required': 'Please enter your email.'})

# forms.py
from django import forms
from django.core.validators import MinLengthValidator, MaxLengthValidator, EmailValidator, RegexValidator

class SubscribeForm(forms.Form):
    first_name = forms.CharField(
        max_length=200,
        required=True,
        validators=[
            MinLengthValidator(2, message="First name must be at least 2 characters long."),
            MaxLengthValidator(200, message="First name cannot exceed 200 characters."),
            RegexValidator(
                regex='^[A-Za-z\s\-]+$',
                message="First name can only contain letters, spaces, and hyphens.",
                code='invalid_first_name'
            )
        ],
        widget=forms.TextInput(attrs={'placeholder': 'First Name'}),
        error_messages={
            'required': 'Please enter your first name.',
        }
    )
    last_name = forms.CharField(
        max_length=200,
        required=True,
        validators=[
            MinLengthValidator(2, message="Last name must be at least 2 characters long."),
            MaxLengthValidator(200, message="Last name cannot exceed 200 characters."),
            RegexValidator(
                regex='^[A-Za-z\s\-]+$',
                message="Last name can only contain letters, spaces, and hyphens.",
                code='invalid_last_name'
            )
        ],
        widget=forms.TextInput(attrs={'placeholder': 'Last Name'}),
        error_messages={
            'required': 'Please enter your last name.',
        }
    )
    email = forms.EmailField(
        required=True,
        validators=[
            EmailValidator(message="Please enter a valid email address."),
        ],
        widget=forms.EmailInput(attrs={'placeholder': 'Email Address'}),
        error_messages={
            'required': 'Please enter your email address.',
        }
    )
    agree_to_policy = forms.BooleanField(
        required=True,
        label="I agree to the privacy policy.",
    )

class CallForm(BaseUserForm):
    organization = forms.CharField(max_length=200, required=True, error_messages={'required': 'Please enter your organization.'})
    income = forms.ChoiceField(
        choices=[('low', 'Low'), ('medium', 'Medium'), ('high', 'High')],
        widget=forms.RadioSelect,
        required=True,
        error_messages={'required': 'Please select your income level.'}
    )
    details = forms.CharField(widget=forms.Textarea, required=True, error_messages={'required': 'Please provide details.'})