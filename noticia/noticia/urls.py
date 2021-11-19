from django.contrib import  admin
from django.db import router
from django.urls import path, include
from redes.views import noticiaViewSet 
from rest_framework import routers
from uuid  import UUID

router = routers.DefaultRouter()
router.register(r'user', noticiaViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api=auth/', include('rest_framework.urls')),
    
]
