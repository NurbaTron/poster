from django.db.models.query import QuerySet
from django.shortcuts import render, HttpResponse
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializars import PosterListSerializer, PosterCreateSerializer, PosterListSerializer, PosterSerializer
from .models import Poster
from rest_framework.generics import RetrieveAPIView, get_object_or_404

# def test(request):
#     return HttpResponse("TEST")


#class based views - cdv

# class Test:
#     def test_method(self):
#         return HttpResponse("TEST")

class TestAPIView(APIView):
    def get(self, *args, **kwargs):
        return Response(data='test')


class PosterListAPIView(APIView):
    def get(self, *args, **kwargs):
        posters = Poster.objects.all()
        posters_json = PosterListSerializer(posters, many=True)
        return Response(data=posters_json.data)

    def post(self, request):
        create_post = request.data.get('poster')
        serializer = PosterCreateSerializer(data=create_post)
        if serializer.is_valid(raise_exception=True):
            serializer_data = serializer.save()
            return Response(f" New data '{serializer_data}' created")

class PosterUpdateAPIView(APIView):
    def put(self, request, pk):
        posters = get_object_or_404(Poster.objects.all(), pk=pk)
        poster = request.data.get('poster')
        serializer = PosterCreateSerializer(instance=posters, data=poster, partial=True)
        if serializer.is_valid():
            serializer_data = serializer.save()
            return Response(f"data '{serializer_data}' is updatet")

class PosterDeleteAPIView(APIView):
    def delete(self, request, pk):
        poster = get_object_or_404(Poster.objects.all(), pk=pk)
        poster.delete()
        return Response("Poster by {} is deletet(like your father)".format(pk))

    




class PosterCreateAPIView(APIView):
    def post(self, request, *args, **kwargs):
        data = request.POST
        serializar_data = PosterCreateSerializer(data=data)
        if serializar_data.is_valid():
            valid_data = serializar_data.save()
            valid_data_json = PosterSerializer(instance=valid_data)
            return Response(data=valid_data_json.data, status=201)
        else:
            return Response(data={
                'messages':'data not valid',
                'errors':serializar_data.errors
            }, status=404)

class PosterRetrieveAPIView(RetrieveAPIView):
    queryset = Poster.objects.all()
    serializer_class = PosterSerializer