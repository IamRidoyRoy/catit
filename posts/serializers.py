from dataclasses import field
from pydoc import ModuleScanner
from rest_framework import serializers
from .models import Post 

class PostSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Post 
        fields = ['id']
