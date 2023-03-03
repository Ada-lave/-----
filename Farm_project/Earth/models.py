from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User





class ProfileUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,default=1)
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=200)
    age = models.CharField(max_length=5)
    address = models.CharField(max_length=1000,default='Екатеринбур')
    number_phone = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    
    
    def __str__(self):
        return self.user.username
    

    