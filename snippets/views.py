from django.shortcuts import render
from rest_framework import generics
from .models import Snippet
from .serializers import SnippetSerializer

# Create your views here.
# ListCreateAPIView is a read-write-delete endpoint that lists all available Snippet instances


class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

# RetrieveUpdateDestroyAPIView is a read-write-delete endpoint for each individual Snippet


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
