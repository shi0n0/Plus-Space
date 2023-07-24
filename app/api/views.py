from rest_framework import generics
from app.models import CustomUser
from app.api.serializer import CustomUserSerializer

class ListView(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all().order_by('-id')

class DetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer