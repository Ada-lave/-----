from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.urls import reverse





class ProfileUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,default=1)
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=200)
    age = models.CharField(max_length=5)
    address = models.CharField(max_length=1000)
    number_phone = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    
    def __str__(self):
        return self.user.username

    def return_absolute_url(self):
        return reverse("user_pk", kwargs={'pk':self.pk})
    

class ProductCard(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    description = models.TextField(max_length=1000)
    category = models.CharField(max_length=50)
    price = models.CharField(max_length=100)


    
class Post(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name='post')
    text = models.CharField(max_length=120)