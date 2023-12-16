from django.db import models
from django.contrib.auth.models import User

class Role(models.Model):
    name = models.CharField(max_length=30, null=False)

    users = models.ManyToManyField(User, related_name="roles", null=True)

    def __str__(self):
        return self.name
