from django.contrib import admin
from .models import CollectionRoute

@admin.register(CollectionRoute)
class CollectionRouteAdmin(admin.ModelAdmin):
    list_display = (
        "route_code",
        "route_date",
        "waste_category",
        "status",
        "company",
        "locality"
    )
    list_filter = ("status", "waste_category", "company", "route_date")
    search_fields = ("route_code", "company__name")
