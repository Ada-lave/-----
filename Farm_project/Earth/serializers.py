from rest_framework import serializers
from .models import OpenProductCard


class TestApi(serializers.ModelSerializer):
    class Meta:
        model = OpenProductCard
        fields = '__all__'
