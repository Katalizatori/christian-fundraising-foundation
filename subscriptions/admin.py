from django.contrib import admin

# Register your models here.
from .models import Subscriber

@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'subscribed_at')
    search_fields = ('email', 'first_name', 'last_name')
    list_filter = ('subscribed_at',)