from django.db import models

# Create your models here.
class BrandModel(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self) -> str:
        return f" {self.name}"