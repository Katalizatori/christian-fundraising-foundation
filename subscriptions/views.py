from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import *
from .models import Subscriber


# Create your views here.
def subscribe_view(request):
    if request.method == "POST":
        print("Form submitted!")  # Debug statement
        form = SubscribeForm(request.POST)
        if form.is_valid():
            print("Form is valid!")  # Debug statement
            # Save the subscriber to the database
            subscriber = Subscriber(
                first_name=form.cleaned_data["first_name"],
                last_name=form.cleaned_data["last_name"],
                email=form.cleaned_data["email"],
            )
            subscriber.save()
            print("Subscriber saved!")  # Debug statement
            messages.success(request, "Thank you for subscribing!")
            return redirect(
                request.META.get("HTTP_REFERER", "index")
            )  # Redirect back to the same page
        else:
            print("Form errors:", form.errors)  # Debug statement
    else:
        form = SubscribeForm()
    return render(request, "index.html", {"form": form})  # Use 'form' consistently
