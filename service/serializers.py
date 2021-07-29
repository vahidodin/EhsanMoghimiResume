from django.db import models
from django.db.models.fields import DateTimeField
from rest_framework.serializers import ModelSerializer, IntegerField , ImageField , CharField , ListField
from .action import convert_to_timestamp

from .models import Service, Image

class ImageSerializers(ModelSerializer):
    image = ImageField(source = 'Image')
    class Meta:
        model=Image
        fields = ['id','image']

# class ServiceSerializers(ModelSerializer):
#     class Meta:
#         model=Service
#         fields = '__all__'

# class DeleteServiceSerializers(ModelSerializer):
#     ServiceId = IntegerField(write_only=True, source='id')
#     class Meta:
#         model=Service
#         fields = ['ServiceId']




class ServiceSerializer(ModelSerializer) : 
    image = ImageSerializers(many = True)
    name = CharField(source = 'Name')
    description = CharField( max_length = 5000 ,source = 'Description')
    price = IntegerField(source = 'Price')


    # def to_representation(self, data):
    #     bb = super(ServiceSerializer, self).to_representation(data)
    #     print("============>" , bb)
    #     print("------------------------")
    #     tm = convert_to_timestamp( bb['created_at'] )
    #     bb['created_at'] = tm
    #     print("****************************************" , bb)

        # cc = zip(bb)
        # print("hi hi : " , cc)
        # for i, k in enumerate(cc):
        #     if i==0:
        #         print("--// >" , cc[k])
                # cc[k]=1
        # return super(ServiceSerializer, self).to_representation(data)

    class Meta : 
        model = Service 
        fields = ['id','image' , 'name' , 'description' , 'price' , 'created_at']
