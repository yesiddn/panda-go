from django.db import models
from waste_categories.models import WasteCategory

class Company(models.Model):
    name = models.CharField(max_length=100)
    waste_categories = models.ManyToManyField(WasteCategory, related_name="companies")

    def __str__(self):
        return self.name
