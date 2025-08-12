from django.db import models

class WasteCategory(models.Model):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name = "Waste Category"
        verbose_name_plural = "Waste Categories"

    def __str__(self):
        return self.name
