from typing import Any
from django.db import models
from brand.models import BrandModel
from django.contrib.auth.models import User

# Create your models here.
class CarModel(models.Model):
    name= models.CharField(max_length=55)
    description = models.TextField()
    price =models.CharField(max_length=55)
    brand = models.ForeignKey(BrandModel, on_delete=models.CASCADE)
    # user = models.ForeignKey(User, on_delete=models.CASCADE, default=User)
    quantity = models.PositiveBigIntegerField(default=10)
    image = models.ImageField(upload_to='car/media/uploads/')
    def __str__(self):
        return f"Car name: {self.name}"

class Comment(models.Model):
    car = models.ForeignKey(CarModel, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=55)
    comment = models.TextField()
    cheated_on = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Comments by {self.name}"

class OrderHistoryModel(models.Model):
    car_name = models.CharField(max_length=55)
    car_description = models.TextField()
    car_price = models.CharField(max_length=55)
    car_brand = models.CharField(max_length=155)
    car_image = models.ImageField(upload_to='car/media/uploads/', blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    purchase_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"name: {self.car_name}"
