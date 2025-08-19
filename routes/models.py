from django.db import models
from localities.models import Locality
from companies.models import Company
from waste_categories.models import WasteCategory

class CollectionRoute(models.Model):
    STATUS_CHOICES = [
        ("planned", "Planned"),
        ("in_progress", "In Progress"),
        ("completed", "Completed"),
        ("canceled", "Canceled"),
    ]

    route_code = models.CharField(max_length=30, unique=True, null=True, blank=True)
    route_date = models.DateField()
    waste_category = models.ForeignKey(
        WasteCategory, on_delete=models.SET_NULL, null=True, blank=True
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="planned")
    capacity_stops = models.IntegerField(null=True, blank=True)
    capacity_weight_kg = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True
    )
    start_time = models.TimeField(null=True, blank=True)
    end_time = models.TimeField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    company = models.ForeignKey(
        Company, on_delete=models.CASCADE, related_name="collection_routes"
    )
    locality = models.ForeignKey(
        Locality,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="collection_routes",
    )

    def __str__(self):
        return f"{self.route_code or self.id}"
