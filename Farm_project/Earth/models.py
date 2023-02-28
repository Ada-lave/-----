from django.db import models

class DataVegetables(models.Model):
    title = models.CharField(max_length=65)
    price = models.IntegerField(max_length=100)
    description = models.TextField(max_length=1000)

class User(models.Model):
    First_name = models.CharField(max_length=65)
    age = models.CharField(max_length=1000)
    Last_name = models.CharField(max_length=128)

class Vegetables(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=1000)
    price = models.IntegerField()

