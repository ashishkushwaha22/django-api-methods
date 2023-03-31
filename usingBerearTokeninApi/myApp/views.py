from django.shortcuts import render

from rest_framework import viewsets, permissions
from .models import Person
from .serializers import PersonSerializer, CustomTokenObtainPairSerializer


# Create your views here.

class PersonViewSet(viewsets.ModelViewSet):

    permission_classes = [permissions.IsAuthenticated]
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


from rest_framework_simplejwt.views import TokenObtainPairView

class ObtainTokenPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


