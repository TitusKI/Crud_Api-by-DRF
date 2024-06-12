from rest_framework import serializers
from .models import BlogPost

class BlogPostSerializer(serializers.ModelSerializer):
    # BlogPostSerializer inherit from serializer class in ModelSerializer
    class Meta:
        model = BlogPost
        fields = ['id', 'title', 'content', 'published_date']