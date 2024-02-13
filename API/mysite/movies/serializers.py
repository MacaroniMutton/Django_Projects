from rest_framework import serializers
from .models import MovieData

class MovieDataSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None, use_url=True)
    class Meta:
        model = MovieData
        fields = ['id', 'name', 'duration', 'rating', 'genre', 'image']