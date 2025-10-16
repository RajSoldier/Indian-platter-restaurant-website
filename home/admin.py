from django.contrib import admin
from home.models import Reservation
from home.models import Chef
from .models import Event,Feedback

# Register your models here.
admin.site.register(Reservation)
admin.site.register(Chef)
admin.site.register(Feedback)


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'location', 'is_upcoming')
    list_filter = ('date', 'location')
    search_fields = ('title', 'description')
    ordering = ('-date',)



