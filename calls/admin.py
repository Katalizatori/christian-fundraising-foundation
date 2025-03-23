from django.contrib import admin
from .models import CallRequest

@admin.register(CallRequest)
class CallRequestAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'surname', 'email', 'phone', 'organisation_name', 'support_needs', 'created_at')
    search_fields = ('first_name', 'surname', 'email', 'organisation_name')
    list_filter = ('created_at',)