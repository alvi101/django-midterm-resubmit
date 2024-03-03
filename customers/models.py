from django.db import models
from django.contrib.auth.models import User

# Create your models here.
""""
User accounts created using Django User model
"""


class PurchaseHistory(models.Model):
    car_image = models.ImageField()
    car_name = models.CharField(max_length=200)
    car_brand = models.CharField(max_length=200)
    price = models.IntegerField()

    user = models.ForeignKey(User, on_delete=models.CASCADE)
