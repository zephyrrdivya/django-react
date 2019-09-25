from clients.models import Client
from rest_framework import viewsets, permissions
from .serializers import ClientSerializer

# Client Viewset


class ClientViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = ClientSerializer

    def get_queryset(self):
        return self.request.user.clients.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
