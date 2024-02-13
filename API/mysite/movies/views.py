from django.shortcuts import render
from .serializers import MovieDataSerializer
from .models import MovieData
from rest_framework import viewsets
# Create your views here.

class MovieDataViewSet(viewsets.ModelViewSet):
    queryset = MovieData.objects.all()
    serializer_class = MovieDataSerializer

class ActionViewSet(viewsets.ModelViewSet):
    queryset = MovieData.objects.filter(genre="action")
    serializer_class = MovieDataSerializer

class ComedyViewSet(viewsets.ModelViewSet):
    queryset = MovieData.objects.filter(genre="comedy")
    serializer_class = MovieDataSerializer