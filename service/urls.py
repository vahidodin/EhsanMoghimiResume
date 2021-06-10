from django.urls import path
from .views import AddService, AddImage, GetService, GetImage, DeleteSerivce

urlpatterns = [
    path('AddService', AddService.as_view(), name='AddService'),
    path('GetService', GetService.as_view(), name='GetService'),
    path('DeleteService', DeleteSerivce.as_view(), name='DeleteService'),
    path('AddImage', AddImage.as_view(), name='AddImage'),
    path('GetImage', AddImage.as_view(), name='GetImage'),


]
