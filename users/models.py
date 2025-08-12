from django.contrib.auth.models import AbstractUser
from django.db import models
from companies.models import Company
from localities.models import Locality

class User(AbstractUser):
    locality = models.ForeignKey(Locality, on_delete=models.SET_NULL, null=True, blank=True)
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True, blank=True, related_name='users') # New field

    def __str__(self):
        return self.username