from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import ProfileUser

@receiver(post_save,sender=User)
def save_user_profile(sender, instance,created, **kwargs):
    if created:
        profile = ProfileUser()
        profile.user = instance
        if 'age' in instance.__dict__:
            profile.age = instance.__dict__['age']
        profile.save()