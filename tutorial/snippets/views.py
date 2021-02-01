from django.shortcuts import render
from rest_framework import status
from django.http import Http404
from rest_framework.response import Response
from .models import Snippet
from .serializers import SnippetSerializer
from rest_framework import generics

# REST framework provides two wrappers you can use to write API views.

# The @api_view decorator for working with function based views.
# The APIView class for working with class-based views.

# To handle URLs like this: http://example.com/api/items/4.json.

# Create your views here.
class SnippetList(generics.ListCreateAPIView):

    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
        
class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer