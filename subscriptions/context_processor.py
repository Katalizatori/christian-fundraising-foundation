from .forms import SubscribeForm

def subscribe_form(request):
    print(f"Context processor called for path: {request.path}")  # Debug statement
    return {
        'subscribe_form': SubscribeForm()
    }