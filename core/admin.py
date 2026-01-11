from django.contrib import admin

from .models import Item


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ("title", "type", "status", "location", "date", "reporter")
    list_filter = ("type", "status")
    search_fields = ("title", "description", "location", "contact_name", "contact_email", "contact_phone")
