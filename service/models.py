from django.db import models
from django_jalali.db import models as jmodels
import os

def get_upload_path(instance,filename):
    return os.path.join(f"{instance.serviceId.name}",filename)

class Service(models.Model):
    STATUSID = [
        (1,"pending"),
        (2,"confirmed"),
        (3,"rejected"),
    ]

    name=models.CharField(max_length=20)
    description=models.TextField()
    status = models.IntegerField(choices=STATUSID, default=1)
    price=models.IntegerField()
    created_at = jmodels.jDateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Image(models.Model):
    serviceId=models.ForeignKey(Service, on_delete=models.CASCADE, related_name='image')
    image=models.ImageField(upload_to=get_upload_path)

    def __str__(self):
        return f"{self.serviceId.name}-{self.id}"



