from clients.models import Client
from clients.serializers import ClientSerializer
from rest_framework import generics


class ClientListCreate(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
