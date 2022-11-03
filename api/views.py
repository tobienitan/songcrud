from django.shortcuts import render

from api.models import Artiste
from api.serializers import ArtisteSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class ArtisteList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        Artistes = Artiste.objects.all()
        serializer = ArtisteSerializer(Artiste, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ArtisteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Create your views here.

class ArtisteDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Artiste.objects.get(pk=pk)
        except Artiste.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        Artiste = self.get_object(pk)
        serializer = ArtisteSerializer(Artiste)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        Artiste = self.get_object(pk)
        serializer = ArtisteSerializer(Artiste, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        Artiste = self.get_object(pk)
        Artiste.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)