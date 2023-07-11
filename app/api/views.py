from django.shortcuts import render
from rest_framework import generics
from app.models import UserProfile
from app.api.serializer import UserProfileSerializer

class ListView(generics.ListCreateAPIView):
    queryset = UserProfile.objects.all().order_by('-id')

class DetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer