from django.db import models
from waste_categories.models import WasteCategory

class Company(models.Model):
    name = models.CharField(max_length=100)
    waste_categories = models.ManyToManyField(WasteCategory, related_name="companies")

    class Meta:
        verbose_name = "Company"
        verbose_name_plural = "Companies"

    def __str__(self):
        return self.name
