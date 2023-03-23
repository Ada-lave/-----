from django.contrib import admin
from .models import *

'''Отображение базы данных в админ панели'''
admin.site.register(ProfileUser)
admin.site.register(ProductCard)
admin.site.register(ProductCardOpen)
