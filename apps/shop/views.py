from rest_framework import viewsets, permissions

from shop.models import Clients, Specialist, CheckIn
from shop.serializers import ClientsSerializer, SpecialistSerializer, CheckInSerializer


class ClientsViewSet(viewsets.ModelViewSet):
    queryset = Clients.objects.all()
    serializer_class = ClientsSerializer
    permission_classes = [permissions.IsAuthenticated]


class SpecialistViewSet(viewsets.ModelViewSet):
    queryset = Specialist.objects.all()
    serializer_class = SpecialistSerializer
    permission_classes = [permissions.IsAdminUser]


class CheckInViewSet(viewsets.ModelViewSet):
    queryset = CheckIn.objects.all()
    serializer_class = CheckInSerializer
    permission_classes = [permissions.IsAdminUser]
