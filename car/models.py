from django.db import models
from brand.models import Brand


class Car(models.Model):
    car_name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.IntegerField()
    quantity = models.IntegerField()
    thumbnail = models.ImageField(upload_to='media/')

    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.brand.name} {self.car_name}'
