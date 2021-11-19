from django.db import models
from rest_framework import fields, serializers, generics
from .models import noticia 


class noticiaSerialzer(serializers.ModelSerializer):
    class Meta:
        model = noticia
        fields = '__all__'

class noticiaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = noticia.objects.all()
    