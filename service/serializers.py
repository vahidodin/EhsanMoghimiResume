from django.db import models
from rest_framework.serializers import ModelSerializer, IntegerField

from .models import Service, Image

class ImageSerializers(ModelSerializer):
    class Meta:
        model=Service
        fields = '__all__'


class ServiceSerializers(ModelSerializer):
    class Meta:
        model=Service
        fields = '__all__'

class DeleteServiceSerializers(ModelSerializer):
    ServiceId = IntegerField(write_only=True, source='id')
    class Meta:
        model=Service
        fields = ['ServiceId']

