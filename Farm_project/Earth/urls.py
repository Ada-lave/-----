from django.urls import path
from .views import *
app_name = "Earth"

urlpatterns = [
    path('profile', show_profile, name='profile'),
]