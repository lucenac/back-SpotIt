from django.contrib import admin

from .models import Item


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ("title", "status", "location", "event_date", "reporter")
    list_filter = ("status",)
    search_fields = ("title", "description", "location", "contact_info")
