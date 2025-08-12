from django.db import models

class Locality(models.Model):
    name = models.CharField(max_length=120)
    code = models.CharField(max_length=20, null=True, blank=True)
    city = models.CharField(max_length=120)
    state = models.CharField(max_length=120, null=True, blank=True)
    country = models.CharField(max_length=120)
    timezone = models.CharField(max_length=64, null=True, blank=True)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Locality"
        verbose_name_plural = "Localities"

    def __str__(self):
        return self.name
