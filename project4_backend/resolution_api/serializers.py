from rest_framework import serializers 
from .models import Resolution 

class ResolutionSerializer(serializers.ModelSerializer): # serializers.ModelSerializer just tells django to convert sql to JSON
    class Meta:
        model = Resolution # tell django which model to use
        fields = ('id', 'title', 'image', 'description', 'category', 'accomplished') # tell django which fields to include
