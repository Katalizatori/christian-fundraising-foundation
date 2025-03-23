from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .forms import CallRequestForm

def book_call(request):
    if request.method == 'POST':
        form = CallRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_page')  # Redirect to a success page
    else:
        form = CallRequestForm()
    return render(request, 'book-call.html', {'form': form})

from django.shortcuts import render

def success_page(request):
    return render(request, 'success.html')