from django.db import models
from django.conf import settings
from localities.models import Locality
from django.utils import timezone
from waste_categories.models import WasteCategory
from routes.models import CollectionRoute

class Request(models.Model):
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("approved", "Approved"),
        ("assigned", "Assigned"),
        ("in_route", "In Route"),
        ("rescheduled", "Rescheduled"),
        ("canceled", "Canceled"),
    ]

    request_date = models.DateTimeField(default=timezone.now)
    collection_date = models.DateField()
    address_snapshot = models.JSONField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")
    status_reason = models.CharField(max_length=255, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    locality = models.ForeignKey(Locality, on_delete=models.CASCADE)
    waste_category = models.ForeignKey(
        WasteCategory, on_delete=models.PROTECT
    )
    route = models.ForeignKey(CollectionRoute, on_delete=models.SET_NULL, null=True, blank=True, related_name='requests')

    def __str__(self):
        return f"Request {self.id} - {self.status}"
