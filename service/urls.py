from django.urls import path

from .views import ServiceViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'services', ServiceViewSet , basename = 'service')
urlpatterns = router.urls


# urlpatterns = [

# ]
