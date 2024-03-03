from django.db import models
from car.models import Car

# Create your models here.


class Comment(models.Model):
    name = models.CharField(max_length=200)
    date_posted = models.DateField(auto_now_add=True)
    body = models.TextField()

    car = models.ForeignKey(Car, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} -> {self.body}'
