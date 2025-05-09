from django.contrib import admin
from django.utils.html import format_html
from .models import Training

class TrainingAdmin(admin.ModelAdmin):
    list_display = ('name', 'event_dates', 'is_active', 'image_preview', 'created_on')
    list_filter = ('is_active', 'start_datetime')
    search_fields = ('name', 'event_id', 'description')
    readonly_fields = ('created_on', 'image_preview')
    fieldsets = (
        ('Basic Information', {
            'fields': ('event_id', 'name', 'description', 'url')
        }),
        ('Date & Time', {
            'fields': ('start_datetime', 'end_datetime'),
            'classes': ('wide',)
        }),
        ('Media', {
            'fields': ('main_image', 'image_preview'),
            'classes': ('wide',)
        }),
        ('Status', {
            'fields': ('is_active',),
            'classes': ('wide',)
        }),
    )
    
    def event_dates(self, obj):
        return f"{obj.start_datetime.strftime('%b %d, %Y')} - {obj.end_datetime.strftime('%b %d, %Y')}"
    event_dates.short_description = 'Event Dates'
    
    def image_preview(self, obj):
        if obj.main_image:
            return format_html('<img src="{}" style="max-height: 200px;"/>', obj.main_image.url)
        return "-"
    image_preview.short_description = 'Preview'

admin.site.register(Training, TrainingAdmin)