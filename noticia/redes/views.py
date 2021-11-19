from typing import Generic
from django.shortcuts import render
from rest_framework import viewsets
from .models import noticia
from .serializer import noticiaSerialzer
import uuid



# Create your views here.

class noticiaViewSet(viewsets.ModelViewSet):
   queryset = noticia.objects.all()
   serializer_class = noticiaSerialzer
    

