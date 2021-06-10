from django.shortcuts import render
from .models import Service, Image

from .serializers import ServiceSerializers, ImageSerializers, DeleteServiceSerializers
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework import status


class AddService(CreateAPIView):
    serializer_class = ServiceSerializers
    def post(self, request, *args, **kwargs):
        serializer = ServiceSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'ok'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GetService(ListAPIView):
    serializer_class = ServiceSerializers
    queryset = Service.objects.all()

class GetImage(ListAPIView):
    serializer_class = ImageSerializers
    queryset = Image.objects.all()


class DeleteSerivce(CreateAPIView):
    serializer_class = DeleteServiceSerializers
    def get_object(self,*args, **kwargs):
        try:
            return Service.objects.get(*args, **kwargs)
        except Service.DoesNotExist:
            return Response("یافت نشد")

    def post(self, request, *args, **kwargs):
        id = request.data.get('ServiceId')
        instance = self.get_object(id=id)
        if instance:
            instance.delete()
            return Response("حذف با موفقیت انجام شد")  

class AddImage(CreateAPIView):
    serializer_class = ImageSerializers
    def post(self, request, *args, **kwargs):
        serializer = ImageSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'ok'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        


