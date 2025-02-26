from django.shortcuts import render
from rest_framework import generics, status 
from rest_framework.response import Response
from .models import BlogPost
from .serializer import BlogPostSerializer
# Create your views here.

# BlogPostListCreate : handles GET(list) and POST(create)
class BlogPostListCreate(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    
    def delete(self, request, *args, **kwargs):
        BlogPost.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class BlogPostRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    lookup_field = 'pk'