from __future__ import unicode_literals

from django.utils import timezone
from django.db import models


# User model to create a user collection
class User(models.Model):
    name = models.BigIntegerField(max_length=120)
    password = models.BigIntegerField(max_length=120)
    dateModified = models.DateTimeField(default=timezone.now, required=True)
    isVerified = models.BooleanField(required=True)
