from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .serializers import ResolutionSerializer
from .models import Resolution

class ResolutionList(generics.ListCreateAPIView):
    queryset = Resolution.objects.all().order_by('id') # tell django how to retrieve all objects from the DB, order by id ascending
    serializer_class = ResolutionSerializer # tell django what serializer to use

class ResolutionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Resolution.objects.all().order_by('id')
    serializer_class = ResolutionSerializer
