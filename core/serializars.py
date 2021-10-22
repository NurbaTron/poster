from rest_framework.serializers import Serializer
from core.models import Poster
from rest_framework import serializers

class PosterListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poster
        fields = ('id', 'title', 'description')


class PosterCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poster
        fields = ['title', 'description']

    def chek(self, data):
        return Poster.objects.filter(**data)

    def update(self, instance, data):
        instance.title = data.get("title", instance.title)
        instance.description = data.get("description", instance.description)
        instance.save()
        return instance


class PosterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poster
        fields = ['id', 'title', 'description', 'photo']
