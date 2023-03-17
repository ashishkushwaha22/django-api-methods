from django.shortcuts import render

from rest_framework import viewsets, permissions
from .models import Person
from .serializers import PersonSerializer


# Create your views here.

class PersonViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


