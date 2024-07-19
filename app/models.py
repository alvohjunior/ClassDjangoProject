from django.db import models


# Create your models here.
class Agents(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    age = models.IntegerField()
    location = models.CharField(max_length=30)
    gender = models.CharField(max_length=10)

    def __str__(self):
        return self.name
