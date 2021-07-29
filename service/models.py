from django.db import models
from django_jalali.db import models as jmodels
import os

def get_upload_path(instance,filename):
    return os.path.join(f"ServicePictures/{instance.ServiceId.Name}",filename)

class Service(models.Model):
    STATUSID = [
        (0,"pending"),
        (1,"confirmed"),
        
    ]

    Name=models.CharField(max_length=20)
    Description=models.TextField()
    Status = models.IntegerField(choices=STATUSID, default=0)
    Price=models.IntegerField()
    created_at = models.DateTimeField()

    def __str__(self):
        return self.Name


class Image(models.Model):
    ServiceId=models.ForeignKey(Service, on_delete=models.CASCADE, related_name='image')
    Image=models.ImageField(upload_to=get_upload_path)

    def __str__(self):
        return f"{self.ServiceId.Name}-{self.id}"



