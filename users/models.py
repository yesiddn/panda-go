from django.contrib.auth.models import AbstractUser
from django.db import models
from localities.models import Locality

class User(AbstractUser):
    locality = models.ForeignKey(Locality, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.username