from django.db import models
from django.contrib.postgres.fields import JSONField

# Create your models here.

class CreateUser(models.Model):
    name = models.CharField(max_length=200)
    data = JSONField()

    def __str__(self):
        return self.name