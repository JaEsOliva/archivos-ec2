from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Archivo
from .serializers import ArchivoSerializer

class ArchivoViewSet(viewsets.ModelViewSet):
    queryset = Archivo.objects.all().order_by('-creado')
    serializer_class = ArchivoSerializer
