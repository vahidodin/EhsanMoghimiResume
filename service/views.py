from django.shortcuts import render
from .models import Service, Image
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework import status


# class AddService(CreateAPIView):
#     serializer_class = ServiceSerializers
#     def post(self, request, *args, **kwargs):
#         serializer = ServiceSerializers(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'message': 'ok'}, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class GetService(ListAPIView):
#     serializer_class = ServiceSerializers
#     queryset = Service.objects.all()

# class GetImage(ListAPIView):
#     serializer_class = ImageSerializers
#     queryset = Image.objects.all()

# class DeleteSerivce(CreateAPIView):
#     serializer_class = DeleteServiceSerializers
#     def get_object(self,*args, **kwargs):
#         try:
#             return Service.objects.get(*args, **kwargs)
#         except Service.DoesNotExist:
#             return Response("یافت نشد")

#     def post(self, request, *args, **kwargs):
#         id = request.data.get('ServiceId')
#         instance = self.get_object(id=id)
#         if instance:
#             instance.delete()
#             return Response("حذف با موفقیت انجام شد")  

# class AddImage(CreateAPIView):
#     serializer_class = ImageSerializers
#     def post(self, request, *args, **kwargs):
#         serializer = ImageSerializers(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'message': 'ok'}, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

from .models import Service
from django.shortcuts import get_object_or_404
from .serializers import ServiceSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from .action import ApiResult


class ServiceViewSet(viewsets.ViewSet):
    
    def list(self, request):
        queryset = Service.objects.filter(Status = 1)
        serializer = ServiceSerializer(queryset, many=True)
        rep = ApiResult()
        rep = rep.content
        rep['data'] = serializer.data
        rep['message'] = ""
        return Response(rep , status=status.HTTP_200_OK)

        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Service.objects.filter(Status = 1)
        service = get_object_or_404(queryset, pk=pk)
        serializer = ServiceSerializer(service)
        if service : 
            rep = ApiResult()
            rep = rep.content
            rep['data'] = serializer.data
            rep['message'] = ""
            return Response(rep , status=status.HTTP_200_OK)

        rep = ApiResult()
        rep = rep.Badstatus
        rep['message'] = "محصول یافت نشد"
        return Response(rep , status=status.HTTP_404_NOT_FOUND)
