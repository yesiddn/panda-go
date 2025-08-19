from django.contrib import admin
from .models import Request


@admin.register(Request)
class RequestAdmin(admin.ModelAdmin):
    list_display = (
        "request_date",
        "collection_date",
        "waste_category",
        "status",
        "user",
        "locality",
        "route"
    )
