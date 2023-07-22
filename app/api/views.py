from rest_framework import generics
from app.models import User
from app.api.serializer import UserSerializer

class ListView(generics.ListCreateAPIView):
    queryset = User.objects.all().order_by('-id')

class DetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer