# subscriptions/views.py
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from .forms import SubscribeForm
from .models import Subscriber
from .services import MailchimpService

@require_POST
@csrf_exempt
def subscribe_view(request):
    form = SubscribeForm(request.POST)
    if form.is_valid():
        first_name = form.cleaned_data["first_name"]
        last_name = form.cleaned_data["last_name"]
        email = form.cleaned_data["email"]
        
        # Save to local database
        subscriber = Subscriber(
            first_name=first_name,
            last_name=last_name,
            email=email,
        )
        subscriber.save()
        
        # Add to Mailchimp
        mailchimp_service = MailchimpService()
        success, response = mailchimp_service.add_subscriber(
            email=email,
            first_name=first_name,
            last_name=last_name
        )
        
        if success:
            return JsonResponse({
                "success": True, 
                "message": "Thank you for subscribing!"
            })
        else:
            # Log error but still show success to user
            print(f"Mailchimp error: {response}")
            return JsonResponse({
                "success": True,
                "message": "Thank you for subscribing! (Note: There was a minor issue with our email service)"
            })
    else:
        errors = {}
        for field in form.errors:
            errors[field] = form.errors[field][0]
        return JsonResponse(
            {
                "success": False,
                "error": "Please correct the errors below",
                "errors": errors,
            },
            status=400,
        )